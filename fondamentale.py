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

    # trouve l'indice de la fondamentale
    index = np.argmax(mag_fft_signal)

    # trouve la fréquence de la fondamentale
    fondamentale_frequence = freqs[index]

    # trouve l'amplitude de la fondamentale
    fondamentale_amplitude = mag_fft_signal[index] / len(fft_signal)

    # trouve la phase de la frequence fondamentale
    fondamentale_phase = phase_fft_signal[index]
    fondamentale_frequence = np.abs(freqs[index])
    #print(f"Frequency: {fondamentale_frequence:.2f} Hz, Amplitude: {fondamentale_amplitude:.2f}, Phase: {fondamentale_phase:.2f} radians")
    return fondamentale_amplitude,fondamentale_phase, fondamentale_frequence,fft_signal_shift
