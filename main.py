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

    freq_fundamental, harmonic_amplitude, harmonic_phases, fft_signal,freqs = fct_DFT(signal,sample_rate)
    # graphique du FFT du signal
    # x = np.arange(num_frames)
    # plt.plot(x,signal)
    # plt.title('Signal audio originale')
    # plt.xlabel('Fréquence')
    # plt.ylabel('Amplitude')
    #
    # plt.show()
    #
    # #graphique du FFT du signal
    # x = np.arange(-(num_frames/2),num_frames/2,1)
    # #plt.plot(x, np.abs(fft_signal))
    # plt.plot(np.abs(fft_signal))
    # plt.title('FFT du signal audio')
    # plt.xlim(65000, 95000)
    # plt.xlabel('Fréquence')
    # plt.ylabel('Amplitude')
    # plt.show()

    # fq= ((freqs / 2)-1)
    # plt.stem(fq, harmonic_amplitude)
    # plt.xlabel('Fréquence (Hz)')
    # plt.ylabel('Amplitude')
    # plt.title('Amplitude des harmoniques')
    # plt.show()

    plt.tight_layout()
    plt.show()


