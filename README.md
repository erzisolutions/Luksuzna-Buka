# 🎧 LUKSUZNA BUKA™ — AI-Powered Audio Mastering Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/erzi-ai/luksuzna-buka)](https://github.com/erzi-ai/luksuzna-buka/stargazers)
[![CI Status](https://github.com/erzi-ai/luksuzna-buka/actions/workflows/ci.yml/badge.svg)](https://github.com/erzi-ai/luksuzna-buka/actions)
[![Try it online](https://img.shields.io/badge/🚀_LIVE-DEMO-green)](https://luksuzna-buka.hf.space)

> **LUKSUZNA BUKA™** je modularna AI platforma za audio mastering, transkripciju na BCS jezicima, analizu, upsampling i generativne efekte — spremna za studio, livestream, podcast i kvantne eksperimente.

---

## 🚀 Ključne Značajke

- 🎚️ AI Mastering Engine (EQ, kompresija, limiter, stereo M/S)
- 🇧🇦 BCS Transkripcija + dijalekt + sentiment analiza (Whisper finetune)
- 🧪 Workflowi: Podcast, GameAudio, Genre Morph, Quantum Mastering
- 🧠 Generativni efekti (AudioLDM, Suno.ai, Udio)
- 🎮 VR/AR Mix Interface + Web GUI + CLI + API
- 🔄 Auto-update sistem i verzionisanje
- 💡 WebRTC kolaboracija + Feedback + projekti u oblaku
- 🪙 Blockchain metadata + ISRC tagging + Atmos
- 🧩 Plugin podrška: CLAP, VST3, LV2, Pedalboard

---

## 📁 Struktura Projekta

```bash
LUKSUZNA_BUKA/
├── gui.py               # Streamlit GUI
├── api_server.py        # REST API
├── launcher.py          # CLI meni
├── webapp/              # Web upload & dashboard
├── workflows/           # Mastering, podcast, gameaudio, quantum...
├── ml/                  # AI modeli: RL, TTS, genre morph
├── bcs_processing/      # Transkripcija, dijalekt, sentiment
├── metadata/            # ISRC, blockchain, atmos
├── plugins/             # CLAP/VST/LV2/Pedalboard loaderi
├── docs/                # PDF + HTML dokumentacija
├── visualization/       # Spectral dashboards, VR, AR
└── .github/workflows/   # CI/CD setup (lint, test)
```

---

## ⚙️ Pokretanje

```bash
# Pokretanje GUI
streamlit run gui.py

# REST API server
python api_server.py

# CLI meni
python launcher.py

# Web interfejs (offline)
open webapp/web_interface.html
```

---

## 🧠 Preporučeni Open-Source Alati

| Alat          | Opis                                      |
|---------------|-------------------------------------------|
| Matchering    | Audio matching/mastering (RMS, stereo...) |
| Spleeter      | Vokal/instrument izolacija                |
| Librosa       | Analiza zvuka (mel, spectral...)          |
| Demucs        | Source separation (Facebook AI)           |
| AudioCraft    | Generativni AI od Meta                    |
| Common Voice  | Dataset za govornu transkripciju          |

---

## 🔄 Auto-Update Sistem

```bash
python utils/updater.py
```

✔️ Backup starih verzija  
✔️ Preuzimanje ZIP updata  
✔️ Overwrite verzija + restart

---

## 🌐 GitHub Pages Dokumentacija

🖥️ Dostupna preko:  
📄 [`/docs/index.html`](https://yourusername.github.io/luksuzna-buka)

---

## 🧪 Primjeri Workflowa

- `workflow_a.py`: Limiter + QA
- `workflow_podcast.py`: Podcast mastering + transkripcija
- `workflow_restore.py`: Denoise, upsample, dereverb
- `workflow_genre_morph.py`: Transformacija žanra
- `workflow_bcs_podcast.py`: BCS dijalekt + speaker labeling
- `workflow_quantum.py`: Kvantna analiza zvuka

---

## 📦 Instalacija

```bash
pip install luksuzna-buka
```

---

## 🛡 Licenca

MIT & GPL Dual License  
> Koristi, remixaj, forkaj – i podijeli nazad.

---

## 🤝 Pridruži se

📣 Prijavi bug, zatraži feature ili pošalji PR!  
📧 Kontakt: erzi.solutions@gmail.com