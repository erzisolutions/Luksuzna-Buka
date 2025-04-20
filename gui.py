import streamlit as st
import numpy as np
import tempfile
from io.loader import load_audio, save_audio
from mastering.limiter import lookahead_limiter
from analysis.qa_engine import QAGate
from pathlib import Path
import soundfile as sf
import json
import matplotlib.pyplot as plt

st.set_page_config(page_title="Erzi Mastering Codex", layout="centered")

st.title("🎚️ ERZI MASTERBOARD – AI Mastering GUI")
st.markdown("Upload audio, run mastering, see QA score, and download your 🔥 master.")

uploaded_file = st.file_uploader("🎵 Upload audio file", type=["wav", "mp3", "flac", "ogg"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = Path(tmp.name)

    st.audio(uploaded_file, format="audio/wav")

    if st.button("🚀 Run Mastering"):
        audio, sr = load_audio(tmp_path)
        mastered = lookahead_limiter(audio.copy(), -1.0)
        qa = QAGate(sr)
        report = qa.evaluate(mastered, sr)

        st.subheader("📊 QA Report")
        st.json(report)

        # waveform
        st.subheader("📈 Waveform")
        fig, ax = plt.subplots()
        ax.plot(mastered[0], label="Mastered L", alpha=0.7)
        if mastered.shape[0] > 1:
            ax.plot(mastered[1], label="Mastered R", alpha=0.7)
        ax.legend()
        st.pyplot(fig)

        # save
        out_path = Path("master_output.wav")
        save_audio(out_path, mastered, sr)

        with open(out_path, "rb") as f:
            st.download_button("💾 Download Master", f, file_name="Erzi_Master.wav")

