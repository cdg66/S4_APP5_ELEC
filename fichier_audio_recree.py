import wave
import numpy as np
import matplotlib.pyplot as plt

def fct_recree_signale(synth, taux):

    wavefile = wave.open('bruit.wav', 'w')
    wavefile.setnchannels(1)  # mono
    wavefile.setsampwidth(2)  # 16 bits
    wavefile.setframerate(taux)
    for s in synth:
        wavefile.writeframesraw(np.int16(s).tobytes())

    wavefile.close()

