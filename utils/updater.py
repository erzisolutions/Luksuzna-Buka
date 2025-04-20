
import os, requests, zipfile, io, shutil
from datetime import datetime
from pathlib import Path

UPDATE_URL = "https://your-server.com/luksuzna_buka_update.zip"
VERSION_FILE = Path("VERSION")
BACKUP_DIR = Path("backup_versions")

def check_current_version():
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()
    return "0.0.0"

def backup_current():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"luksuzna_buka_backup_{timestamp}"
    shutil.copytree(".", backup_path, ignore=shutil.ignore_patterns('backup_versions', '__pycache__', '*.pyc'))
    print(f"✅ Backup saved to: {backup_path}")

def update_from_zip(url):
    print(f"🔄 Downloading update from {url}...")
    r = requests.get(url)
    if r.status_code != 200:
        print("❌ Update download failed.")
        return
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        for file in z.namelist():
            if file.startswith("omni_codex_vSigma/") or file.startswith("LUKSUZNA_BUKA/"):
                z.extract(file, ".")
    print("✅ Update applied.")

def run_update():
    backup_current()
    update_from_zip(UPDATE_URL)
    print("🔁 Restart app to apply updates.")

if __name__ == "__main__":
    print(f"🧠 Current version: {check_current_version()}")
    confirm = input("Proceed with update? (y/n): ")
    if confirm.lower() == "y":
        run_update()
