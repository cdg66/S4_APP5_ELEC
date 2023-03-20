import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def fct_harmoniques2(signal, sample_rate):
    window = np.hanning(len(signal))
    windowed_signal = signal * window

    # Calcule fft
    fft_signal = np.fft.fft(windowed_signal)
    #fft_signal_shift = np.fft.fftshift(fft_signal)
    frequences = np.fft.fftfreq(len(fft_signal)) * sample_rate
    module_signale = np.abs(fft_signal)
    module_phase = np.angle(fft_signal)

    # trouver les 32 harmoniques
    n = 33
    harmonique_frequence = [0] * n
    harmonique_amplitude = [0] * n
    harmonique_phase = [0] * n

    for i in range(33):
        index = np.argmax(module_signale) * (i + 1)
        harmonique_frequence[i] = frequences[index]
        harmonique_amplitude[i] = module_signale[index] / len(fft_signal)
        harmonique_phase[i] = module_phase[index]
        print(f"Harmoniques {i} Frequency: {harmonique_frequence[i]:.2f} Hz, Amplitude: {harmonique_amplitude[i]:.2f},"f" module_phase: {harmonique_phase[i]:.2f} radians")

    # sommation des 32 harmoniques
    x = np.arange(160000)
    som_32_harmoniques = np.zeros(len(fft_signal))
    for i in range(33):
        som_32_harmoniques += harmonique_amplitude[i] * np.sin(2 * np.pi * (harmonique_frequence[i]/sample_rate) * x + harmonique_phase[i])

    return harmonique_amplitude, harmonique_phase, harmonique_frequence, som_32_harmoniques,fft_signal