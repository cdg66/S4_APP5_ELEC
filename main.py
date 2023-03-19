import wave
import numpy as np
import matplotlib.pyplot as plt
from harmoniques import *
from fondamentale import *
from enveloppe_temporel import *
from fichier_audio_recree import *
from Ouvrir_fichier_audio import *

num_frames, sample_rate, frames, signal = parametre_fichier_audio()

harmonique_amplitude, harmonique_phase, harmonique_frequence,sin_sum = fct_harmoniques(signal, sample_rate)

fondamentale_amplitude, fondamentale_phase, fondamentale_frequence, fft_signal_shift = fct_fondamentale(signal,sample_rate)

enveloppe_signale = fct_enveloppe(signal, sample_rate)
signale_recree = fct_recree_signale(sin_sum,enveloppe_signale)

def fct_graph_fft(graph_fft):
    if graph_fft == True:
        # graphique du signal originale
        x = np.arange(num_frames)
        plt.plot(x,signal)
        plt.plot(x,enveloppe_signale)
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
        axs[0].stem(20 * np.log10(harmonique_amplitude))
        axs[0].set_title('Module de X1')

        axs[1].stem(harmonique_phase)
        axs[1].set_title('Angle de X1')


        axs[1].stem(harmonique_phase)
        axs[1].set_title('Angle de X1')

        plt.tight_layout()
        plt.show()

        # plot du sinus somme
        plt.plot(sin_sum)
        plt.title('sinus somme')
        plt.xlabel('Fréquence')
        plt.ylabel('Amplitude')
        plt.show()
    else:
        return 0

def fct_graph_harmoniques(graph_harmoniques):
    if graph_harmoniques == True:
        harmonique_amplitude_1 = 20 * np.log10(harmonique_amplitude)
        plt.stem(harmonique_frequence, np.abs(harmonique_amplitude_1))
        plt.xlabel('Fréquence')
        plt.ylabel('Amplitude')
        plt.show()


        harmonique_phase_1 = (harmonique_phase)
        plt.stem(harmonique_frequence, harmonique_phase_1)
        plt.xlabel('Fréquence')
        plt.ylabel('Phase')
        plt.show()
    else:
        return 0




fct_graph_fft(graph_fft=False)

fct_graph_harmoniques(graph_harmoniques=True)

fct_harmoniques(signal, sample_rate)


