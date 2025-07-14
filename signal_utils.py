import numpy as np

def rms(values):
    return np.sqrt(np.mean(np.square(values)))


def phase_shift(signal1, signal2, fs, freq=60):
    n_samples = len(signal1)
    corr = np.correlate(signal1 - np.mean(signal1), signal2 - np.mean(signal2), mode='full')
    lag = np.argmax(corr) - (n_samples - 1)

    # Calculate time shift
    time_shift = lag / fs
    period = 1 / freq
    phase = (time_shift / period) * 360  # time shift → degrees

    # Normalize to [-180, 180]
    phase = (phase + 180) % 360 - 180
    return phase

def estimate_frequency(signal, fs):
    # Zero-crossing method
    crossings = np.where(np.diff(np.signbit(signal)))[0]
    if len(crossings) < 2:
        return 0
    periods = np.diff(crossings[::2])  # every other crossing ≈ 1 full period
    avg_period = np.mean(periods) / fs  # convert samples to seconds
    return 1 / avg_period
