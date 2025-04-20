import os
import subprocess
import sys

# 🛠️ Always run from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MENU = {
    "1": ("Masteruj jedan fajl", "python workflows/workflow_a.py"),
    "2": ("Batch Mastering", "python workflows/batch_master.py"),
    "3": ("Stem Mastering (Demucs)", "python workflows/workflow_stem.py"),
    "4": ("Run QA Gate on Master", "python analysis/qa_runner.py"),
    "5": ("Generate A/B Export", "python utils/ab_exporter.py"),
    "6": ("EXIT", "exit")
}

def main():
    while True:
        print("\n== ERZI'S AI MASTERING ARSENAL ==")
        for k, v in MENU.items():
            print(f"{k}. {v[0]}")
        choice = input("Izbor: ").strip()
        if choice == "6":
            break
        elif choice in MENU:
            subprocess.run(MENU[choice][1], shell=True)
        else:
            print("❌ Nevažeći izbor.")

if __name__ == "__main__":
    main()
