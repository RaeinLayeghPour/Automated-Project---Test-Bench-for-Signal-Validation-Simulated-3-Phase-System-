# 🔌 Automated Test Bench for Signal Validation (Simulated 3-Phase System)

A Python-based test automation framework for simulating and validating 3-phase AC signals under various conditions including frequency variation, phase shift, and noise. Designed as a signal validation tool for electrical engineering applications such as inverter testing, motor control, and power system QA.

---

## 📋 Features

- ✅ Simulates clean and noisy 3-phase sinusoidal waveforms
- ✅ Automated test validation using `pytest`
- ✅ Phase shift detection using cross-correlation
- ✅ Frequency estimation using zero-crossing
- ✅ RMS verification
- 📈 Signal visualization with `matplotlib`
- 🧪 Extensible for testing distortion, clipping, and harmonics

---

## 🧠 Why This Project?

This project was built to bridge the gap between theory and practice in electrical engineering. It brings together:

- Python-based test automation (`pytest`)
- Core signal processing concepts (RMS, frequency, phase)
- Realistic simulation of 3-phase signals and their imperfections
- A clean and modular codebase, ready for extension

---

## 🛠️ Tech Stack

- Python 3.13+
- `pytest` – testing framework
- `numpy` – numerical signal generation
- `pandas` – data structuring
- `matplotlib` – waveform visualization

