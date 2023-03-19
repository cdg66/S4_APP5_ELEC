import wave
import numpy as np
import matplotlib.pyplot as plt

def fct_recree_signale(sin_sum,enveloppe_normalisee):
    signale_recree = np.multiply(sin_sum,enveloppe_normalisee)

    return signale_recree
