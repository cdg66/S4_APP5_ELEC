import wave
import numpy as np

def fct_re(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal):
   # generation du re
    x = np.arange(160000)
    note_re = np.zeros(len(fft_signal))
    for i in range(33):
        note_re += harmonique_amplitude[i] * np.sin(2 * np.pi * ((harmonique_frequence[i] / 1.06) * 0.667 / sample_rate) * x + harmonique_phase[i])

    re_synthese = enveloppe * note_re
    re_synthese = re_synthese * 32000 / np.max(np.abs(re_synthese))  # normalise la sythese audio

    wavefile = wave.open('re_synthese.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)

    for patate in re_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())
    wavefile.close()
