from pyloudnorm import Meter
import numpy as np
import json
from pathlib import Path

class QAGate:
    def __init__(self, sr):
        self.meter = Meter(sr)

    def evaluate(self, audio: np.ndarray, sr: int) -> dict:
        loudness = self.meter.integrated_loudness(audio)
        peak = np.max(np.abs(audio))
        plr = peak - loudness
        score = 0
        score += 2 if loudness >= -15 and loudness <= -13 else 0
        score += 2 if peak <= 1.0 else 0
        score += 2 if plr >= 8 else 0
        score += 2  # placeholder for spectral match
        score += 2  # placeholder for dropout/silence
        return {
            "loudness": loudness,
            "peak": peak,
            "plr": plr,
            "score": score,
            "passed": score == 10
        }
