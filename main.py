import wave
import numpy as np
import matplotlib.pyplot as plt
from DFT import *

with wave.open('note_guitare_LAd.wav', 'rb') as wav_file:
    # nb d'échantillon du fichier
    num_frames = wav_file.getnframes()

    # Retourne la fréquence d'échantillonage en Hz
    sample_rate = wav_file.getframerate()

    # lit tout le contenu du fichier et stock les amplitudes dans frames
    frames = wav_file.readframes(num_frames)

    #Convertir les échantillons audio en une série temporelle de valeurs d'amplitude
    signal = np.frombuffer(frames, dtype=np.int16)

    freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies, fft_signal = fct_DFT(signal,sample_rate)
    # graphique du FFT du signal
    x = np.arange(num_frames)
    plt.plot(x,signal)
    plt.title('Signal audio originale')
    plt.xlabel('Fréquence')
    plt.ylabel('Amplitude')
    plt.show()

    # graphique du FFT du signal
    freq = np.fft.fftshift(np.fft.fftfreq(160000))
    plt.plot(freq, np.abs(fft_signal))
    plt.title('FFT du signal audio')

    plt.xlabel('Fréquence')
    plt.ylabel('Amplitude')
    plt.show()

    fig, axs = plt.subplots(2, 1)
    t_fft1 = np.linspace(-0.5, 0.5, 79999, endpoint=False)
    axs[0].stem(harmonic_amplitude)
    axs[0].set_title('Module de X1')

    axs[1].stem(harmonic_phases)
    axs[1].set_title('Angle de X1')

    plt.tight_layout()
    plt.show()

    # fq= ((freqs / 2)-1)
    # plt.stem(fq, harmonic_amplitude)
    # plt.xlabel('Fréquence (Hz)')
    # plt.ylabel('Amplitude')
    # plt.title('Amplitude des harmoniques')
    # plt.show()
#x = np.arange(-(num_frames/2),num_frames/2,1)
    # x = np.arange(-(len(harmonic_amplitude)/2), (len(harmonic_amplitude)/2), 1)
    #plt.plot(x, np.abs(fft_signal))
    # plt.xlim(65000, 95000)
