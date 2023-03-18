import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
def fct_harmoniques(signal, sample_rate):
    # Appliquer une fenêtre de Hanning
    window = np.hanning(len(signal))
    windowed_signal = signal * window

    # Calculer la DFT
    fft_signal = np.fft.fft(windowed_signal)
    freqs = np.fft.fftfreq(len(fft_signal)) * sample_rate

    # Trouver les maximums locaux dans le spectre
    #peaks, _ = find_peaks(np.abs(fft_signal), distance=100)
    peaks, _ = find_peaks(np.abs(fft_signal)[:len(fft_signal) // 2], distance=100)

    # Garder les 32 plus grands maximums locaux

    peaks = peaks[np.argsort(np.abs(fft_signal[peaks]))[::-1]][:32]

    # Déterminer l'amplitude relative de chaque harmonique
    harmonique_amplitude = np.abs(fft_signal[peaks]) / len(signal)

    # Calculer la phase de chaque harmonique
    harmonique_phase = np.angle(fft_signal[peaks])

    # Déterminer la fréquence de chaque harmonique
    harmonique_frequence = freqs[peaks]
    # sommations des sinus
    for i in range(32):
        sin_sum = harmonique_amplitude[i] * (np.sin(2* np.pi * harmonique_frequence[i] *len(signal) + harmonique_phase[i]))

    #Retourner les amplitudes, phases et fréquences des 32 harmoniques
    for i in range(len(harmonique_amplitude)):
        print(
            f"Harmonic {i + 1}: Frequency: {harmonique_frequence[i]:.2f} Hz, Amplitude: {harmonique_amplitude[i]:.2f}, Phase: {harmonique_phase[i]:.2f} radians")

    return harmonique_amplitude, harmonique_phase, harmonique_frequence, sin_sum

# def fct_harmoniques(signal, sample_rate):
#     # Appliquer une fenêtre de Hanning
#     window = np.hanning(len(signal))
#     windowed_signal = signal * window
#
#     # Calculer la DFT
#     fft_signal = np.fft.fft(windowed_signal)
#     freqs = np.fft.fftfreq(len(fft_signal)) * sample_rate
#
#     # Déterminer l'indice de la fondamentale
#     index_fondamentale = np.argmax(np.abs(fft_signal))
#
#     # Déterminer l'amplitude relative de chaque harmonique
#     harmonique_amplitude = np.abs(fft_signal) / len(signal)
#
#     # Calculer la phase de chaque harmonique
#     harmonique_phase = np.angle(fft_signal)
#
#     # Déterminer la fréquence de chaque harmonique
#     index_harmoniques = np.arange(2, 33)
#     harmonique_frequence = index_harmoniques * freqs[index_fondamentale]
#
#     #Retourner les amplitudes, phases et fréquences des 32 harmoniques
#     for i in range(len(harmonique_amplitude)):
#         print(
#             f"Harmonic {i + 1}: Frequency: {harmonique_frequence[i]:.2f} Hz, Amplitude: {harmonique_amplitude[i]:.2f}, Phase: {harmonique_phase[i]:.2f} radians")
#
#     return harmonique_amplitude, harmonique_phase, harmonique_frequence



