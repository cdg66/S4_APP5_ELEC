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

    # Trouver les maximums locaux dans la plage des fréquences d'harmoniques à +/- 500 Hz autour de la fréquence fondamentale
    f_1 = 466  # Fréquence fondamentale
    freq_range = 25  # plage des fréquences d'harmoniques à +/- 500 Hz autour de la fréquence fondamentale
    harmonics_freqs = [f_1 * i for i in range(1, 33)]  # les fréquences théoriques des 32 premiers harmoniques

    peaks, _ = find_peaks(np.abs(fft_signal)[:len(fft_signal) // 2], distance=100)

    # Garder les maximums locaux dans la plage des fréquences d'harmoniques à +/- 500 Hz autour de la fréquence fondamentale
    peaks_in_range = []
    for p in peaks:
        if abs(harmonics_freqs - freqs[p]).min() <= freq_range:
            peaks_in_range.append(p)

    # Garder les 32 plus grands maximums locaux
    peaks_in_range = np.array(peaks_in_range)
    peaks_in_range = peaks_in_range[np.argsort(np.abs(fft_signal[peaks_in_range]))[::-1]][:32]

    # Déterminer l'amplitude relative de chaque harmonique
    harmonique_amplitude = np.abs(fft_signal[peaks_in_range]) / len(signal)

    # Calculer la phase de chaque harmonique
    harmonique_phase = np.angle(fft_signal[peaks_in_range])

    # Déterminer la fréquence de chaque harmonique
    harmonique_frequence = freqs[peaks_in_range]

    # sommations des sinus
    sin_sum = np.zeros(len(signal))
    for i in range(len(harmonique_amplitude)):
        sin_sum += harmonique_amplitude[i] * np.sin(2 * np.pi * harmonique_frequence[i] * np.arange(len(signal)) + harmonique_phase[i])

        # Normalize sin_sum to have values between -1 and 1
       # sin_sum = sin_sum / np.max(np.abs(sin_sum))

    # Retourner les amplitudes, phases et fréquences des 32 harmoniques
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



