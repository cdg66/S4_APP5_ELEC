import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def fct_enveloppe(signal, sample_rate,som_32_harmoniques):
       filtre = sig.firwin(884, cutoff=np.pi/1000 , fs=sample_rate, pass_zero=True) #ordre, fc , fréquence échantillonage, type de filtre
       enveloppe = sig.lfilter(filtre, 1, np.abs(signal))
       audio_synthese = enveloppe * som_32_harmoniques
       return enveloppe, audio_synthese
