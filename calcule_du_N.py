import math

import numpy as np
w = np.pi/1000
def fct_calcule_N():
    for N in range(1,10000):
        h_w = (1/N)*(math.sin((N*w)/2)/math.sin(w/2))
        if h_w > 0.706 and h_w < 0.708:
            print(N)
            return N