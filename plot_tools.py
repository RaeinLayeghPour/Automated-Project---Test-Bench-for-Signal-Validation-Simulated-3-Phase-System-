import matplotlib.pyplot as plt

def plot_signals(df, title="3-Phase Signals"):
    ax = df.plot(title=title, figsize=(10, 4))
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    plt.tight_layout()
    plt.show()