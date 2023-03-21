import wave
import numpy as np
import matplotlib.pyplot as plt

def fct_fondamentale(signal, sample_rate):
    # calcule la fenetre
    window = np.hanning(len(signal))
    windowed_signal = signal * window

    # Calculer fft
    fft_signal = np.fft.fft(windowed_signal)
    fft_signal_shift = np.fft.fftshift(fft_signal)
    freqs = np.fft.fftfreq(len(fft_signal)) * sample_rate

    mag_fft_signal = np.abs(fft_signal)
    phase_fft_signal = np.angle(fft_signal)
    index = np.argmax(mag_fft_signal)
    fondamentale_frequence = freqs[index]
    fondamentale_amplitude = mag_fft_signal[index] / len(fft_signal)
    fondamentale_phase = phase_fft_signal[index]
    fondamentale_frequence = np.abs(freqs[index])
    return fondamentale_amplitude,fondamentale_phase, fondamentale_frequence,fft_signal_shift
