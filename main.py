import wave
import numpy as np
import matplotlib.pyplot as plt
from harmonique import *
from calcule_du_N import *
from fondamentale import *
from enveloppe_temporel import *
from generer_audio import *
from Ouvrir_fichier_audio import *
#from fct_generer_note import *

signal, sample_rate,num_frames = parametre_fichier_audio()

harmonique_amplitude, harmonique_phase, harmonique_frequence,somme_32_harmoniques = fct_harmoniques2(signal, sample_rate)

fondamentale_amplitude, fondamentale_phase, fondamentale_frequence, fft_signal_shift = fct_fondamentale(signal,sample_rate)

enveloppe, audio_synthese = fct_enveloppe(signal, sample_rate,somme_32_harmoniques)

signale_recree = fct_generer_audio(audio_synthese ,sample_rate)

#fct_generer_note(fondamentale_frequence)

N = fct_calcule_N()

def fct_graph_fft(graph_fft):
    if graph_fft == True:
        # graphique du signal originale
        x = np.arange(num_frames)
        plt.plot(x,signal)
        plt.plot(x, enveloppe)
        #plt.plot(x, audio_synthese)
        plt.title('Signal audio originale')
        plt.xlabel('Échantillons')
        plt.ylabel('Amplitude')
        plt.show()

        # graphique module signal FFT
        freq = np.fft.fftshift(np.fft.fftfreq(160000))
        fft_signal_shift_1 = 20*np.log10(fft_signal_shift)
        plt.plot(freq, np.abs(fft_signal_shift_1))
        plt.title('FFT du signal audio')
        plt.xlabel('Fréquences')
        plt.ylabel('Amplitude')
        plt.show()
    else:
        return 0

def fct_graph_harmoniques(graph_harmoniques):
    if graph_harmoniques == True:

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        ax1.stem(harmonique_frequence, harmonique_amplitude)
        ax1.set_title('Modules des harmoniques')
        ax1.set_yscale('log')
        ax1.set_xlabel("Fréquences en Hz")
        ax1.set_ylabel("Amplitude")

        ax2.stem(harmonique_frequence, harmonique_phase)
        ax2.set_xlabel("Fréquences en Hz")
        ax2.set_title('Phases des harmoniques')
        ax2.set_ylabel("Amplitude")

        plt.tight_layout()
        plt.show()
    else:
        return 0

def fct_graph_synthese_enveloppe(graph_synthese_enveloppe):
    if graph_synthese_enveloppe == True:

        # on fait le graphique de l'enveloppe icite
        x = np.arange(160000)
        plt.plot(x, enveloppe)
        plt.xlabel("Échantillons")
        plt.ylabel("Amplitude")
        plt.show()

        # on fait le graphique de la synthese audio icite
        plt.plot(x, audio_synthese)
        plt.xlabel("Échantillons")
        plt.ylabel("Amplitude")
        plt.show()
    else:
        return 0

fct_graph_fft(graph_fft=True)

fct_graph_harmoniques(graph_harmoniques=False)

fct_graph_synthese_enveloppe(graph_synthese_enveloppe=False)



