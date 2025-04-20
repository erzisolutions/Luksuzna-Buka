<!--
SEO‑KEYWORDS: AI audio mastering, Python mastering suite, Matchering 2.0, automated audio processing, LUFS analysis, BCS transcription, Gradio frontend, FastAPI backend, Docker audio app, Erzi Solutions, Globl Contact GmbH, Luksuzna Buka, open‑source mastering, cloud mastering engine
-->
# 🎧 **LUKSUZNA BUKA™** — AI‑Powered Audio Mastering Suite  
*Studio‑grade mastering • Zero local setup • Built by **Erzi Solutions** & **Globl Contact GmbH***  

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![CI](https://github.com/erzi-ai/luksuzna-buka/actions/workflows/ci.yml/badge.svg)](https://github.com/erzi-ai/luksuzna-buka/actions)  
[![Stars](https://img.shields.io/github/stars/erzi-ai/luksuzna-buka?style=social)](https://github.com/erzi-ai/luksuzna-buka/stargazers)  
[![Live Demo](https://img.shields.io/badge/🚀_LIVE-DEMO-brightgreen)](https://luksuzna-buka.hf.space)

> **LUKSUZNA BUKA™** transforms *any* track—WAV, MP3, FLAC, livestream, podcast—into a fully mastered export (WAV 24‑bit, MP3 320 kbps, FLAC) with AI‑assisted QA so only **10 / 10** results ship to your audience.

---

## ⚡ Feature Highlights
| 🚀 Module | 🔍 What It Does |
|-----------|----------------|
| **AI Mastering Core** | Matchering 2.0 + genre‑aware EQ, multiband compression, stereo enhancer, limiter |
| **Quality Gate (QA Engine)** | LUFS, peak, dynamic range & spectral balance checks—fails tracks that don’t meet spec |
| **Transcription & Analysis** | Multilingual STT for BCS / DE / EN + keyword extraction |
| **Workflow Library** | Pre‑built pipelines: **Podcast**, **Livestream**, **Game Audio**, **Genre Morph**, **Stem Master** |
| **REST API & CLI** | FastAPI server + Python CLI (`launcher.py`) for automation |
| **Gradio / HTML GUI** | Drag‑&‑drop web interface with A↔B “Normal vs Enchanted” toggle |
| **Docker & CI/CD** | One‑command container, GitHub Actions for lint + pytest |
| **MKDocs Docs Site** | Full developer & user manuals ready for GitHub Pages |

---

## 🏗️ System Architecture

```text
            ┌───────────────────────────────────┐
            │          Web Frontend             │
            │  (Gradio / Static HTML GUI)       │
            └───────────────┬───────────────────┘
                            │  HTTP / WebSocket
          ┌─────────────────▼───────────────────┐
          │        FastAPI  Backend  (api_server.py)  │
          └─────────────────┬───────────────────┘
                            │  Python calls
     ┌──────────────────────▼────────────────────────┐
     │              Core Engines                     │
     │  • Mastering Engine  (Matchering, FX)         │
     │  • Analyzer & QA Runner (analysis/)           │
     │  • Transcriber  (utils/stt.py)                │
     │  • Restoration  (restoration/)                │
     └─────────────────┬─────────────────────────────┘
                       │
        ┌──────────────▼──────────────┐
        │      Workflow Manager       │
        │  (workflows/*.py pipelines) │
        └──────────────┬──────────────┘
                       │
              ┌────────▼────────┐
              │  Export System  │
              │  .wav / .mp3 / .flac  │
              └──────────────────┘
```

---

## 📦 Repository Layout
```
├── launcher.py               # Simple CLI launcher
├── api_server.py             # FastAPI backend
├── webapp/                   # Gradio & static HTML GUI
├── workflows/                # Modular processing pipelines
├── analysis/                 # QA engine & audio analyzers
├── restoration/              # Noise/hiss repair modules
├── utils/                    # Helper libs (uploader, updater)
├── docker/                   # Dockerfile & compose
├── docs/                     # MKDocs source
├── tests/                    # PyTest suite
└── mkdocs.yml                # Docs site config
```

---

## ⚙️ Quick Start

```bash
# 1. Clone
git clone https://github.com/erzi-ai/luksuzna-buka.git
cd luksuzna-buka

# 2. Install deps (Python 3.10+)
pip install -r requirements.txt

# 3. Launch GUI
python launcher.py
```

**Docker way**

```bash
docker build -t luksuzna-buka .
docker run -p 7860:7860 luksuzna-buka
```

Then open `http://localhost:7860` and drop your track.

---

## 📝 Documentation

* **User Guide** – `docs/` (served via MKDocs)  
* **API Reference** – `/docs/swagger` once server is running  
* **Workflow Blueprints** – `docs/workflows/`  
* **CI Status** – see badge above  

Live docs site → *enable GitHub Pages from `/docs` branch*

---

## 💻 Programmatic Use

```python
from luksuzna_buka.api_client import MasteringClient

client = MasteringClient("http://localhost:8000")
client.master_track(
    input_path="demo.wav",
    workflow="standard",
    out_format="flac"
)
```

---

## 🤖 Roadmap 2025

- 🔗 **VST Bridge** for real‑time DAW mastering  
- 🛰️ **Cloud Queue** for massive batch jobs  
- 🎛️ **Dynamic Genre Morph** (EDM → Lo‑fi overnight)  
- 🏆 **AI Mix Feedback** with chat‑style suggestions  

*Open an issue or PR to be part of the build crew.* 🚀

---

## 🤝 License

Released under a **modified MIT License** for **Erzi Solutions** & **Globl Contact GmbH** – see [LICENSE](LICENSE).

---

## 📞 Contact & Support
* Email: **kontakt@globl.contat**  
* IG: **@erzi.14**  
* Site: **https://www.globl.contat**

> **“Sound matters. Silence obeys. Luksuzna Buka™ delivers.”**  
> *Star ⭐ the repo if this saved you hours of EQ‑tweaking!* 🎚️
```
