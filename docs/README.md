
# OMNI-CODEX vΣ Documentation

## Overview
OMNI-CODEX is an AI-driven audio mastering and restoration platform with modular architecture.

### Components
- **api_server.py** – Flask REST API (POST /master, GET /status)
- **webapp/web_interface.html** – simple HTML/JS frontend that uses the API
- **gui.py** – Streamlit desktop GUI
- **launcher.py** – CLI menu
- **workflows/** – individual mastering workflows
- **ml/** – machine learning utilities
- **analysis/** – QA and analysis modules

### Running Locally
```bash
pip install -r requirements.txt flask streamlit soundfile torch librosa pyloudnorm
python api_server.py              # starts REST on http://localhost:8000
streamlit run gui.py              # starts Streamlit GUI
```

### API Usage
**POST /master**

| Form field | Description           |
|------------|-----------------------|
| file       | Audio file (.wav...)  |
| workflow   | a / podcast / restore / livestream / genre_morph / gameaudio |

Returns: ZIP with mastered WAV and qa_report.json

**GET /status** → `{ "status":"ok", "version":"vSigma" }`

### Folder Structure
```
.
analysis
config
docker
io
mastering
plugins
restoration
tests
utils
workflows
```
