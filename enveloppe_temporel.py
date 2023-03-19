import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def fct_enveloppe(donne, taux,sin_sum):
#
#
#
#        signal_tempo = abs(donne)
#        fe = taux
#        fc = fe * ((np.pi / 1000) / (2 * np.pi))
#        # lpf_coeffs = firwin(884, fc/(fe/2), window='hamming', pass_zero=True)
#        lpf_coeffs = np.ones(884) / 884
#        output = lfilter(lpf_coeffs, 1, signal_tempo)
#        # output = np.convolve(signal_tempo, lpf_coeffs, mode='same')
#        output = np.divide(output, np.amax(output))  # pour normaliser le signal
#
#        synth = output * sin_sum
#
#        return output, synth

       rate, data = wav.read('note_guitare_LAd.wav')

       # sig.firwin(ordre, fc , fréquence échantillonage, type de filtre
       b = sig.firwin(884, cutoff=np.pi/1000 , fs=rate, pass_zero=True)
       output = sig.lfilter(b, 1, np.abs(data))
       w, h = sig.freqz(b)


       synth = output * sin_sum
       return output, synth
