
from harmonique import *
from calcule_du_N import *
from fondamentale import *
from enveloppe_temporel import *
from generer_audio import *
from Ouvrir_fichier_audio import *
from sol import *
from re_note import *
from mi_be import *
from fa import *

signal, sample_rate,num_frames = parametre_fichier_audio()

harmonique_amplitude, harmonique_phase, harmonique_frequence,somme_32_harmoniques,fft_signal = fct_harmoniques2(signal, sample_rate)

fondamentale_amplitude, fondamentale_phase, fondamentale_frequence, fft_signal_shift = fct_fondamentale(signal,sample_rate)

N = fct_calcule_N()

enveloppe, audio_synthese = fct_enveloppe(signal, sample_rate,somme_32_harmoniques,N)
fct_enveloppe(signal, sample_rate,somme_32_harmoniques,N)

signale_recree = fct_generer_audio(audio_synthese ,sample_rate)
N = fct_calcule_N()

re = fct_re(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal)
fa = fct_fa(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal)
mib = fct_mi_be(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal)
sol = fct_sol(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal)
fct_baathovenize(sol,mib,fa,re, sample_rate)



def fct_graph_fft(graph_fft):
    if graph_fft == True:
        x = np.arange(num_frames)
        plt.plot(x, signal)
        plt.plot(x, enveloppe)
        plt.title('Signal audio originale', fontsize=18)
        plt.xlabel('Échantillons', fontsize=16)
        plt.ylabel('Amplitude', fontsize=16)
        plt.show()

        # plot audio signal FFT
        fft_signal_shift = np.fft.fftshift(np.fft.fft(signal))
        freq = np.fft.fftshift(np.fft.fftfreq(len(fft_signal_shift)))
        fft_signal_shift_db = 20 * np.log10(np.abs(fft_signal_shift))
        freq_hz = freq * len(signal)  # conversion de l'unité des fréquences
        mask = (freq_hz >= -17000) & (freq_hz <= 17000)  # création d'un masque pour filtrer les fréquences

        # create figure and axes objects
        fig, ax1 = plt.subplots()
        ax1.plot(freq_hz[mask], fft_signal_shift_db[mask])
        ax1.set_xlabel('Fréquences (Hz)', fontsize=16)
        ax1.set_ylabel('Amplitude (dB)', fontsize=16)
        ax1.set_title('FFT du signal audio', fontsize=18)
        ax1.tick_params(axis='both', which='major', labelsize=16, width=2)

        plt.show()

    else:
        return 0

def fct_graph_harmoniques(graph_harmoniques):
    if graph_harmoniques == True:

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        ax1.stem(harmonique_frequence, harmonique_amplitude)
        ax1.set_title('Modules des harmoniques', fontsize=18)
        ax1.set_yscale('log')
        ax1.set_xlabel("Fréquences en Hz", fontsize=16)
        ax1.set_ylabel("Amplitude", fontsize=16)
        ax1.tick_params(axis='both', which='major', labelsize=16, width=2)

        ax2.stem(harmonique_frequence, harmonique_phase)
        ax2.set_xlabel("Phases en rad", fontsize=16)
        ax2.set_title('Phases des harmoniques', fontsize=18)
        ax2.set_ylabel("Amplitude", fontsize=16)
        ax2.tick_params(axis='both', which='major', labelsize=16, width=2)

        plt.tight_layout()
        plt.show()

    else:
        return 0

def fct_graph_synthese_enveloppe(graph_synthese_enveloppe):
    if graph_synthese_enveloppe == True:

        # on fait le graphique de l'enveloppe icite
        x = np.arange(160000)
        plt.plot(x, enveloppe)
        plt.title('Enveloppe temporelle', fontdict={'fontsize': 18})
        plt.xlabel("Échantillons", fontdict={'fontsize': 16})
        plt.ylabel("Amplitude", fontdict={'fontsize': 16})
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.show()

        # on fait le graphique de la synthese audio icite
        plt.plot(x, audio_synthese)
        plt.xlabel("Échantillons")
        plt.ylabel("Amplitude")
        plt.show()
    else:
        return 0

fct_graph_fft(graph_fft=False)

fct_graph_harmoniques(graph_harmoniques=False)

fct_graph_synthese_enveloppe(graph_synthese_enveloppe=False)



