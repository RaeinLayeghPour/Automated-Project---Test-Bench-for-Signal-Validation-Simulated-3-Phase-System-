import numpy as np
import pandas as pd

def generate_3phase_signals(freq=60, duration=0.1, fs=10000, noise_amplitude=0.0):
    t = np.arange(0, duration, 1/fs)
    base = 2 * np.pi * freq * t
    signals = {
        'A': np.sin(base + np.deg2rad(0)),
        'B': np.sin(base + np.deg2rad(-120)),
        'C': np.sin(base + np.deg2rad(120)),
    }

    if noise_amplitude > 0: # noise_amplitude = 0.0
        for phase in signals:
            noise = np.random.normal(0, noise_amplitude, size=len(t))
            signals[phase] += noise

    return pd.DataFrame(signals, index=pd.to_timedelta(t, unit='s'))

