import numpy as np
def lookahead_limiter(audio, ceiling=-1.0):
    peak = np.max(np.abs(audio))
    gain = 10**(ceiling / 20) / peak if peak != 0 else 1.0
    return audio * gain
