import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def fct_harmoniques2(donne, taux):
    # calcul du fft ainsi que c'est attribut
    signal_hanning = np.ones(len(donne)) * donne
    signal_fft = np.fft.fft(signal_hanning)
    freqs = np.fft.fftfreq(len(signal_fft)) * taux
    mag = np.abs(signal_fft)
    phase = np.angle(signal_fft)

    # boucle pour trouver les 32 sinusoid principal
    tab_freq = np.zeros(33)
    tab_mag = np.zeros(33)
    tab_phase = np.zeros(33)
    i = 1
    while i <= 33:
        index = np.argmax(mag) * i
        tab_freq[i - 1] = freqs[index]
        tab_mag[i - 1] = mag[index] / len(signal_fft)
        tab_phase[i - 1] = phase[index]
        print(f"Harmoniques {i - 1} Frequency: {tab_freq[i - 1]:.2f} Hz, Amplitude: {tab_mag[i - 1]:.2f},"
              f" Phase: {tab_phase[i - 1]:.2f} radians")
        i += 1

        # addition des 32 sinusoid
    temps = np.arange(160000)
    sin_sum = np.zeros(len(signal_fft))
    for i in range(33):
        sin_sum += tab_mag[i] * np.sin(2 * np.pi * tab_freq[i] * temps + tab_phase[i])

    return tab_mag, tab_phase, tab_freq, sin_sum
    # addition des 32 sinusoid
    # sin_sum = np.zeros(len(signal_fft))
    # for i in range(33):
    #     sin_sum += tab_mag[i] * np.sin(2 * np.pi * tab_freq[i] * temps + tab_phase[i])