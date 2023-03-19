import wave
import numpy as np
import matplotlib.pyplot as plt
from harmonique2 import *
from fondamentale import *
from enveloppe_temporel import *
from fichier_audio_recree import *
from Ouvrir_fichier_audio import *

signal, sample_rate,num_frames = parametre_fichier_audio()

harmonique_amplitude, harmonique_phase, harmonique_frequence,sin_sum = fct_harmoniques2(signal, sample_rate)

fondamentale_amplitude, fondamentale_phase, fondamentale_frequence, fft_signal_shift = fct_fondamentale(signal,sample_rate)

output, synth = fct_enveloppe(signal, sample_rate,sin_sum)
signale_recree = fct_recree_signale(synth ,sample_rate)

def fct_graph_fft(graph_fft):
    if graph_fft == True:
        # graphique du signal originale
        x = np.arange(num_frames)
        plt.plot(x,signal)
        plt.plot(x, output)
        #plt.plot(x, synth)
        plt.title('Signal audio originale')
        plt.xlabel('Fréquence')
        plt.ylabel('Amplitude')
        plt.show()

        # graphique module signal FFT
        freq = np.fft.fftshift(np.fft.fftfreq(160000))
        fft_signal_shift_1 = 20*np.log10(fft_signal_shift)
        plt.plot(freq, np.abs(fft_signal_shift_1))
        plt.title('FFT du signal audio')

        plt.xlabel('Fréquence')
        plt.ylabel('Amplitude')
        plt.show()
    else:
        return 0

def fct_graph_harmoniques(graph_harmoniques):
    if graph_harmoniques == True:
        # amplitude des 32 harmonique
            plt.stem(harmonique_frequence, harmonique_amplitude)
            plt.yscale('log')
            plt.xlabel("Time [s]")
            plt.ylabel("Amplitude en logarithmique")
            plt.show()

            plt.stem(harmonique_frequence, harmonique_phase)
            plt.xlabel("Time [s]")
            plt.ylabel("Amplitude")
            plt.show()

            # plot du sinus somme
            temps = np.arange(160000)
            plt.plot(temps, output)
            plt.xlabel("m")
            plt.ylabel("Amplitude")
            plt.show()

            # plot sytese
            plt.plot(temps, synth)
            plt.xlabel("m")
            plt.ylabel("Amplitude")
            plt.show()
    else:
        return 0

fct_graph_fft(graph_fft=True)

fct_graph_harmoniques(graph_harmoniques=False)



