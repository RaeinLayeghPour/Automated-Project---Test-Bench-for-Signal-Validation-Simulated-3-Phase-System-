import pytest
from signal_generator import generate_3phase_signals
from signal_utils import rms, phase_shift, estimate_frequency
from plot_tools import plot_signals

@pytest.fixture
def signals():
    return generate_3phase_signals(freq=60, duration=0.1, fs=10000)

def test_frequency(signals):
    fs = 10000
    freq = estimate_frequency(signals['A'], fs)
    assert 59.5 <= freq <= 60.5

def test_rms(signals):
    for phase in signals.columns:
        val = rms(signals[phase])
        assert 0.69 <= val <= 0.71  # ideal RMS of sin wave ≈ 0.707

def test_phase_shift(signals):
    fs = 10000
    ab = phase_shift(signals['A'], signals['B'], fs)
    ac = phase_shift(signals['A'], signals['C'], fs)

    assert abs(ab + 120) < 10
    assert abs(ac - 120) < 10


def test_noisy_signal():
    df = generate_3phase_signals(freq=60, duration=0.1, fs=10000, noise_amplitude=0.1)
    plot_signals(df, title="Noisy 3-Phase Signals")

    # basic test: values shouldn't blow up
    for col in df.columns:
        assert df[col].abs().max() < 2