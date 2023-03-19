import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter


def fct_enveloppe(donne, taux,sin_sum):

       signal_tempo = abs(donne)
       fe = taux
       fc = fe * ((np.pi / 1000) / (2 * np.pi))
       # lpf_coeffs = firwin(884, fc/(fe/2), window='hamming', pass_zero=True)
       lpf_coeffs = np.ones(884) / 884
       output = lfilter(lpf_coeffs, 1, signal_tempo)
       # output = np.convolve(signal_tempo, lpf_coeffs, mode='same')
       output = np.divide(output, np.amax(output))  # pour normaliser le signal

       synth = output * sin_sum

       return output, synth
