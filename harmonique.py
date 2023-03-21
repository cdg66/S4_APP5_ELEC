
import numpy as np


def fct_harmoniques2(signal, sample_rate):
    window = np.hanning(len(signal))
    windowed_signal = signal * window

    # Calcule fft
    fft_signal = np.fft.fft(windowed_signal)
    frequences = np.fft.fftfreq(len(fft_signal)) * sample_rate
    module_signale = np.abs(fft_signal)
    module_phase = np.angle(fft_signal)

    # trouver les 32 harmoniques
    n = 33
    harmonique_frequence = [0] * n
    harmonique_amplitude = [0] * n
    harmonique_phase = [0] * n

    for i in range(33):
        j = np.argmax(module_signale) * (i + 1)
        harmonique_frequence[i] = frequences[j]
        harmonique_amplitude[i] = module_signale[j] / len(fft_signal)
        harmonique_phase[i] = module_phase[j]
        print(f"Harmoniques {i} Frequency: {harmonique_frequence[i]:.2f} Hz, Amplitude: {harmonique_amplitude[i]:.2f},"f" module_phase: {harmonique_phase[i]:.2f} radians")

    # somme 32 harmoniques
    x = np.arange(160000)
    som_32_harmoniques = np.zeros(len(fft_signal))
    for i in range(33):
        som_32_harmoniques += harmonique_amplitude[i] * np.sin(2 * np.pi * (harmonique_frequence[i]/sample_rate) * x + harmonique_phase[i])

    return harmonique_amplitude, harmonique_phase, harmonique_frequence, som_32_harmoniques,fft_signal