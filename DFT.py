import wave
import numpy as np
import matplotlib.pyplot as plt
def fct_DFT(signal,sample_rate):

    # Appliquer une fenêtre de Hamming pour meilleur DFT
    window = np.hamming(len(signal))
    windowed_signal = signal * window

    # Calculer la DFT de la série temporelle fenêtrée
    dft = np.fft.fft(windowed_signal)


    # Trouver les fréquences et amplitudes des harmoniques
    freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
    harmonic_indices = np.where(freqs > 0)
    harmonic_freqs = freqs[harmonic_indices]
    harmonic_amplitude = np.abs(dft[harmonic_indices])

    # La phase des harmoniques
    harmonic_phases = np.angle(dft[harmonic_indices])

    # Estimer la fréquence fondamentale
    fundamental_index = np.argmax(harmonic_amplitude)
    freq_fundamental = harmonic_freqs[fundamental_index]

    return freq_fundamental, harmonic_amplitude, harmonic_phases