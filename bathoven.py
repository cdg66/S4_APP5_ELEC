
import numpy as np
import matplotlib.pyplot as plt
def fct_bathoven(fondamentale_transformee, harmonique_amplitude,harmonique_phase,enveloppe,sample_rate, secondes = 4):
    t = np.linspace(0, secondes , int(sample_rate * secondes))
    # gen a La
    Sol = np.zeros(len(t))
    j = 1
    for i in range(len(harmonique_amplitude)):
        Sol = Sol + fct_gen_sin(harmonique_amplitude[i], fondamentale_transformee[0] * j, t, harmonique_phase[i])
        j = j + 1
    plt.plot(t,Sol)
    plt.show()
    return Sol


def fct_gen_sin(amplitude, f, t, phi):
    sin = amplitude * np.sin(2 * np.pi * f * t + phi)
    return sin