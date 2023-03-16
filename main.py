import wave
import numpy as np
import matplotlib.pyplot as plt
from DFT import *

with wave.open('note_basson_plus_sinus_1000_Hz.wav', 'rb') as wav_file:
    # nb d'échantillon du fichier
    num_frames = wav_file.getnframes()

    # Retourne la fréquence d'échantillonage en Hz
    sample_rate = wav_file.getframerate()

    # lit tout le contenu du fichier et stock les amplitudes dans frames
    frames = wav_file.readframes(num_frames)

    # Convertir les échantillons audio en une série temporelle de valeurs d'amplitude
    signal = np.frombuffer(frames, dtype=np.int16)


    freq_fundamental, harmonic_amplitude, harmonic_phases = fct_DFT(signal,sample_rate)

    # Pad the harmonic amplitude and phases arrays with zeros if necessary
    if len(harmonic_amplitude) < len(signal):
        harmonic_amplitude = np.pad(harmonic_amplitude, (0, len(signal) - len(harmonic_amplitude)))
    if len(harmonic_phases) < len(signal):
        harmonic_phases = np.pad(harmonic_phases, (0, len(signal) - len(harmonic_phases)))

    N = len(signal)  # length of the signal
    n1 = np.arange(0, N, 1)  # create an array (start, stop, step)
    t_fft1 = np.linspace(-0.5, 0.5, N, endpoint=False)

    fig, axs = plt.subplots(3, 1)

    # plot the original signal
    axs[0].stem(n1, signal)
    axs[0].set_title('x1')

    # plot the harmonic amplitude
    axs[1].stem(t_fft1, harmonic_amplitude)
    axs[1].set_title('harmonic_amplitude')

    # plot the harmonic phases
    axs[2].stem(t_fft1, harmonic_phases)
    axs[2].set_title('harmonic_phases')

    plt.tight_layout()
    plt.show()




