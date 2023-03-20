import numpy as np
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter
import scipy.signal as sig
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
def fct_enveloppe(signal, sample_rate,som_32_harmoniques,N):
       abs_signal = abs(signal)
       [1] * (N // N)
       a = np.full((N,), 1) / N
       enveloppe = np.convolve(abs_signal, a, mode='same')
       audio_synthese = enveloppe * som_32_harmoniques
       audio_synthese = audio_synthese * 32000 / np.max(np.abs(audio_synthese)) #normalise la sythese audio

       return enveloppe, audio_synthese
