import soundfile as sf
from pathlib import Path

def load_audio(path: Path, sr=44100):
    audio, samplerate = sf.read(str(path), always_2d=True)
    return audio.T, samplerate

def save_audio(path: Path, audio, sr: int):
    sf.write(str(path), audio.T, sr)
