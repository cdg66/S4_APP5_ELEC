import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt



def fct_enveloppe(signal, sample_rate):

       # sig.firwin(ordre, fc , fréquence échantillonage, passe bas
       N = 884
       filtre = sig.firwin(N, cutoff = 22.05 , fs=sample_rate, pass_zero=True)
       enveloppe_signale = sig.lfilter(filtre, 1, np.abs(signal)) # appliquer le signale dans ton filtre
       #enveloppe_normalisee = enveloppe_signale / np.max(enveloppe_signale)
       freq_normalise, gain = sig.freqz(filtre) # retourne fréquence normalisé, module(gain)



       # plt.plot(freq_normalise/np.pi, np.abs(gain))
       # plt.xlabel('Fréquence normalisée')
       # plt.ylabel('Gain')
       # plt.title('Réponse en fréquence d\'un filtre FIR')
       # plt.show()
       #
       # plt.plot(signal, label='Signal')
       # plt.plot(enveloppe_signale, label='Enveloppe')
       # plt.legend()
       # plt.show()
       #
       #
       # # Tracé de la réponse en fréquence
       # fig, ax = plt.subplots()
       # ax.plot(freq_normalise, 20 * np.log10(abs(gain)))
       # ax.set(title='Réponse en fréquence du filtre passe-bas',
       #        xlabel='Fréquence (rad/sample)', ylabel='Gain (dB)')
       # ax.grid(True)
       # plt.show()

       return enveloppe_signale