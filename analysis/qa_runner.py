from io.loader import load_audio
from analysis.qa_engine import QAGate
from pathlib import Path
import json

def run():
    path = input("Putanja do fajla: ").strip()
    audio, sr = load_audio(Path(path))
    gate = QAGate(sr)
    report = gate.evaluate(audio, sr)
    out_dir = Path("qa_output")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "qa_report.json").write_text(json.dumps(report, indent=2))
    print("✅ QA završena.")

if __name__ == "__main__":
    run()
