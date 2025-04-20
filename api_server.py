"""
Simple Flask API for OMNI‑CODEX vΣ
Endpoints:
  POST /master  - audio mastering with workflow param
  GET  /status  - health check
"""
import os, tempfile, uuid, io, zipfile
from pathlib import Path
from flask import Flask, request, jsonify, send_file
from workflows import workflow_a, workflow_podcast, workflow_restore, workflow_livestream, workflow_genre_morph, workflow_gameaudio

WORKFLOW_MAP = {
    "a": workflow_a,
    "podcast": workflow_podcast,
    "restore": workflow_restore,
    "livestream": workflow_livestream,
    "genre_morph": workflow_genre_morph,
    "gameaudio": workflow_gameaudio,
}

app = Flask(__name__)

@app.route("/status")
def status():
    return {"status": "ok", "version": "vSigma"}, 200

@app.route("/master", methods=["POST"])
def master_endpoint():
    if "file" not in request.files:
        return {"error": "No file"}, 400
    file = request.files["file"]
    wf_key = request.form.get("workflow", "a").lower()
    if wf_key not in WORKFLOW_MAP:
        return {"error": "Unknown workflow"}, 400
    # Save temp
    tmp_dir = Path(tempfile.mkdtemp())
    in_path = tmp_dir / file.filename
    file.save(in_path)
    # Run workflow (each returns (out_path, qa_json))
    run_func = WORKFLOW_MAP[wf_key].run  # each workflow has run(path, out_dir)
    out_dir = tmp_dir / "out"
    out_dir.mkdir()
    run_func(in_path, out_dir)
    # Expect master wav
    master_file = next(out_dir.glob("*master.wav"), None)
    qa_json_file = next(out_dir.glob("*qa*.json"), None)
    if not master_file:
        return {"error": "Mastering failed"}, 500
    # Create zip to stream
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(master_file, master_file.name)
        if qa_json_file:
            zf.write(qa_json_file, qa_json_file.name)
    zip_buffer.seek(0)
    return send_file(zip_buffer, mimetype="application/zip",
                     download_name=f"{master_file.stem}_package.zip")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
