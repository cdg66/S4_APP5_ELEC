import wave
import numpy as np
import matplotlib.pyplot as plt

def fct_fondamentale(signal, sample_rate):
    # Appliquer une fenêtre de Hanning
    window = np.hanning(len(signal))
    windowed_signal = signal * window

    # Calculer la DFT
    fft_signal = np.fft.fft(windowed_signal)
    fft_signal_shift = np.fft.fftshift(fft_signal)
    freqs = np.fft.fftfreq(len(fft_signal)) * sample_rate

    #  calcule les magnitudes et phase des coefficients de la DFT.
    mag_fft_signal = np.abs(fft_signal)
    phase_fft_signal = np.angle(fft_signal)

    # détermine l'indice de la fondamentale
    index = np.argmax(mag_fft_signal)

    # détermine la fréquence de la fondamentale
    fondamentale_frequence = freqs[index]

    # détermine l'amplitude relative de la fréquence dominante, en normalisant par la longueur du signal d'entrée.
    fondamentale_amplitude = mag_fft_signal[index] / len(fft_signal)

    # détermine la phase de la frequence fondamentale
    fondamentale_phase = phase_fft_signal[index]
    fondamentale_frequence = np.abs(freqs[index])
    #print(f"Frequency: {fondamentale_frequence:.2f} Hz, Amplitude: {fondamentale_amplitude:.2f}, Phase: {fondamentale_phase:.2f} radians")
    return fondamentale_amplitude,fondamentale_phase, fondamentale_frequence,fft_signal_shift
