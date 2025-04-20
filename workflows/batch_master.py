import os
from pathlib import Path
from io.loader import load_audio, save_audio
from mastering.limiter import lookahead_limiter
from analysis.qa_engine import QAGate
import json

def run():
    folder = input("Folder sa fajlovima: ").strip()
    output_dir = Path("batch_output")
    output_dir.mkdir(exist_ok=True)
    for file in os.listdir(folder):
        if not file.endswith(('.wav', '.mp3', '.flac', '.ogg')):
            continue
        path = Path(folder) / file
        audio, sr = load_audio(path)
        mastered = lookahead_limiter(audio.copy(), -1.0)
        qa = QAGate(sr)
        report = qa.evaluate(mastered, sr)
        fname = path.stem
        if report["passed"]:
            save_audio(output_dir / f"{fname}_master.wav", mastered, sr)
            (output_dir / f"{fname}_qa.json").write_text(json.dumps(report, indent=2))
        else:
            (output_dir / f"{fname}_fail.json").write_text(json.dumps(report, indent=2))

if __name__ == "__main__":
    run()
