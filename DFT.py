import wave
import numpy as np
import matplotlib.pyplot as plt
def fct_DFT(signal,sample_rate):

    # Calculer la DFT
    fft_signal = np.fft.fftshift(np.fft.fft(signal))

    # Appliquer une fenêtre de Hamming
    window = np.hamming(len(fft_signal))
    windowed_signal = fft_signal * window

    # Trouver les fréquences et amplitudes des harmoniques
    freqs = np.fft.fftfreq(len(windowed_signal), 1/sample_rate)
    harmonic_indices = np.where(freqs > 0)
    harmonic_freqs = freqs[harmonic_indices]
    harmonic_amplitude = np.abs(windowed_signal[harmonic_indices])

    # La phase des harmoniques
    harmonic_phases = np.angle(windowed_signal[harmonic_indices])

    # Trouver fréquence fondamentale
    fundamental_index = np.argmax(harmonic_amplitude)
    freq_fundamental = harmonic_freqs[fundamental_index]

    return freq_fundamental, harmonic_amplitude, harmonic_phases, fft_signal,freqs

