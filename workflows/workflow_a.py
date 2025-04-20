from io.loader import load_audio, save_audio
from mastering.limiter import lookahead_limiter
from analysis.qa_engine import QAGate
from pathlib import Path
import json

def run():
    path = input("Putanja do fajla: ").strip()
    audio, sr = load_audio(Path(path))
    mastered = lookahead_limiter(audio.copy(), -1.0)
    qa = QAGate(sr)
    report = qa.evaluate(mastered, sr)
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    if report["passed"]:
        save_audio(out_dir / "master.wav", mastered, sr)
        (out_dir / "qa_report.json").write_text(json.dumps(report, indent=2))
        print("✅ Master sačuvan.")
    else:
        (out_dir / "qa_fail.json").write_text(json.dumps(report, indent=2))
        print("❌ QA nije prošao.")

if __name__ == "__main__":
    run()
