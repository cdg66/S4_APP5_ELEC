import wave
import numpy as np
import matplotlib.pyplot as plt
from harmoniques import *
from fondamentale import *
from enveloppe_temporel import *

with wave.open('note_guitare_LAd.wav', 'rb') as wav_file:
    # nb d'échantillon du fichier
    num_frames = wav_file.getnframes()

    # Retourne la fréquence d'échantillonage en Hz
    sample_rate = wav_file.getframerate()

    # lit tout le contenu du fichier et stock les amplitudes dans frames
    frames = wav_file.readframes(num_frames)

    #Convertir les échantillons audio en une série temporelle de valeurs d'amplitude
    signal = np.frombuffer(frames, dtype=np.int16)

    harmonique_amplitude, harmonique_phase, harmonique_frequence,sin_sum = fct_harmoniques(signal, sample_rate)

    fondamentale_amplitude, fondamentale_phase, fondamentale_frequence, fft_signal_shift = fct_fondamentale(signal,sample_rate)
    w = np.pi/1000
    N = get_filter_order(w,sample_rate )
    print(N)


    def fct_graph_fft(graph_fft):
        if graph_fft == True:
            # graphique du signal originale
            x = np.arange(num_frames)
            plt.plot(x,signal)
            plt.title('Signal audio originale')
            plt.xlabel('Fréquence')
            plt.ylabel('Amplitude')
            plt.show()

            # graphique module signal FFT
            freq = np.fft.fftshift(np.fft.fftfreq(160000))
            plt.plot(freq, np.abs(fft_signal_shift))
            plt.title('FFT du signal audio')

            plt.xlabel('Fréquence')
            plt.ylabel('Amplitude')
            plt.show()
            # graphique phase signal FFT
            fig, axs = plt.subplots(2, 1)
            t_fft1 = np.linspace(-0.5, 0.5, 79999, endpoint=False)
            axs[0].stem(harmonic_amplitude)
            axs[0].set_title('Module de X1')

            axs[1].stem(harmonic_phases)
            axs[1].set_title('Angle de X1')


            axs[1].stem(harmonic_phases)
            axs[1].set_title('Angle de X1')

            plt.tight_layout()
            plt.show()
        else:
            return 0

    def fct_graph_harmoniques(graph_harmoniques):
        if graph_harmoniques == True:
            plt.stem(harmonique_frequence, harmonique_amplitude)
            plt.xlabel('Fréquence')
            plt.ylabel('Amplitude')
            plt.show()

            plt.stem(harmonique_frequence, harmonique_phase)
            plt.xlabel('Fréquence')
            plt.ylabel('Phase')
            plt.show()
        else:
            return 0

    fct_graph_fft(graph_fft=False)

    fct_graph_harmoniques(graph_harmoniques=True)


