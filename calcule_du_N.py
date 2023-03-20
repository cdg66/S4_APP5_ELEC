import math
import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from math import sin, sqrt
w = np.pi/1000
N = 1
def fct_calcule_N():
    for N in range(1,10000):
        h_w = (1/N)*(math.sin((N*w)/2)/math.sin(w/2))
        if h_w > 0.706 and h_w < 0.708:
            print(N)
            return N