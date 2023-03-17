import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def fct_DFT(signal, sample_rate):
    # Appliquer une fenêtre de Hamming
    window = np.hamming(len(signal))
    windowed_signal = signal * window

    # Calculer la DFT
    fft_signal = np.fft.fftshift(np.fft.fft(windowed_signal))



    # Trouver la fondamentale
    autocorr = np.correlate(signal, signal, mode='full')
    freq_fundamental_index = np.argmax(autocorr[1:]) + 1

    # Convertir l'indice de la fréquence fondamentale en Hz
    freq_fundamental = sample_rate / freq_fundamental_index
    fundamental_amplitude = np.abs(fft_signal[freq_fundamental_index]) / len(windowed_signal) * 2

    # Trouver les indices des harmoniques
    n_harmonics = 32
    peaks, _ = find_peaks(np.abs(fft_signal)[:len(fft_signal)//2], distance=1000, height=1000)
    harmonic_indices = []
    for i in range(n_harmonics):
        harmonic_index = int(round(peaks[0] * (i+1)))
        harmonic_indices.append(harmonic_index)

    # Calculer l'amplitude, la phase et la fréquence de chaque harmonique
    harmonic_amplitude = np.abs(fft_signal[harmonic_indices]) / len(fft_signal) * 2
    harmonic_phases = np.angle(fft_signal[harmonic_indices])
    #harmonic_frequencies = harmonic_indices / len(windowed_signal) * sample_rate
    harmonic_frequencies = [index / len(fft_signal) * sample_rate for index in harmonic_indices]
    harmonic_frequencies = [index / len(fft_signal) * sample_rate for index in harmonic_indices]

    # Retourner les résultats
    return freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies, fft_signal
























#
#
# # le nb d'hamonic est 32 dans la problematique, c'est à modifier dans mon code
#     # Calculer la DFT
#     fft_signal = np.fft.fftshift(np.fft.fft(signal))
#
#     # Appliquer une fenêtre de Hamming
#     window = np.hamming(len(fft_signal))
#     windowed_signal = fft_signal * window
#
#     # Trouver la fondamentale
#     autocorr = np.correlate(signal, signal, mode='full')
#     freq_fundamental_index = np.argmax(autocorr[1:]) + 1
#
#     # Convertir l'indice de la fréquence fondamentale en Hz
#     freq_fundamental = sample_rate / freq_fundamental_index
#     fundamental_amplitude = np.abs(windowed_signal[freq_fundamental_index]) / len(windowed_signal) * 2
#
#
#     # Trouver les indices des harmoniques
#     n_harmonics = 32
#     harmonic_indices = []
#     for i in range(n_harmonics):
#         harmonic_index = int(round(peaks[0] * (i+1)))
#         harmonic_indices.append(harmonic_index)
#
#     # Calculer l'amplitude, la phase et la fréquence de chaque harmonic
#     harmonic_amplitude = np.abs(windowed_signal[harmonic_indices]) / len(windowed_signal) * 2
#     harmonic_phases = np.angle(windowed_signal[harmonic_indices])
#     harmonic_frequencies = harmonic_indices / len(windowed_signal) * sample_rate
#
#
#
#     return freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies
#
#
# # # Trouver les fréquences et amplitudes des harmoniques
# # freqs = np.fft.fftfreq(len(windowed_signal), 1 / sample_rate)
# # harmonic_indices = np.where(freqs > 0)
# # harmonic_freqs = freqs[harmonic_indices]
# # harmonic_amplitude = np.abs(windowed_signal[harmonic_indices])
#
#
# # # La phase des harmoniques
# # harmonic_phases = np.angle(windowed_signal[harmonic_indices])
# #
# # # Trouver fréquence fondamentale
# # fundamental_index = np.argmax(harmonic_amplitude)
# # freq_fundamental = harmonic_freqs[fundamental_index]























#
#
# # le nb d'hamonic est 32 dans la problematique, c'est à modifier dans mon code
#     # Calculer la DFT
#     fft_signal = np.fft.fftshift(np.fft.fft(signal))
#
#     # Appliquer une fenêtre de Hamming
#     window = np.hamming(len(fft_signal))
#     windowed_signal = fft_signal * window
#
#     # Trouver la fondamentale
#     autocorr = np.correlate(signal, signal, mode='full')
#     freq_fundamental_index = np.argmax(autocorr[1:]) + 1
#
#     # Convertir l'indice de la fréquence fondamentale en Hz
#     freq_fundamental = sample_rate / freq_fundamental_index
#     fundamental_amplitude = np.abs(windowed_signal[freq_fundamental_index]) / len(windowed_signal) * 2
#
#
#     # Trouver les indices des harmoniques
#     n_harmonics = 32
#     harmonic_indices = []
#     for i in range(n_harmonics):
#         harmonic_index = int(round(peaks[0] * (i+1)))
#         harmonic_indices.append(harmonic_index)
#
#     # Calculer l'amplitude, la phase et la fréquence de chaque harmonic
#     harmonic_amplitude = np.abs(windowed_signal[harmonic_indices]) / len(windowed_signal) * 2
#     harmonic_phases = np.angle(windowed_signal[harmonic_indices])
#     harmonic_frequencies = harmonic_indices / len(windowed_signal) * sample_rate
#
#
#
#     return freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies
#
#
# # # Trouver les fréquences et amplitudes des harmoniques
# # freqs = np.fft.fftfreq(len(windowed_signal), 1 / sample_rate)
# # harmonic_indices = np.where(freqs > 0)
# # harmonic_freqs = freqs[harmonic_indices]
# # harmonic_amplitude = np.abs(windowed_signal[harmonic_indices])
#
#
# # # La phase des harmoniques
# # harmonic_phases = np.angle(windowed_signal[harmonic_indices])
# #
# # # Trouver fréquence fondamentale
# # fundamental_index = np.argmax(harmonic_amplitude)
# # freq_fundamental = harmonic_freqs[fundamental_index]