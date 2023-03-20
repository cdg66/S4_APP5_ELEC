import wave
import numpy as np
def fct_mi_be(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal):
#generation du mi_be
    x = np.arange(23000)
    note_mi_be = np.zeros(len(x))
    for i in range(33):
        note_mi_be += harmonique_amplitude[i] * np.sin(2 * np.pi * ((harmonique_frequence[i]/1.06)*0.707 / sample_rate) * x + harmonique_phase[i])

    mi_be_synthese = enveloppe[0:len(x)] * note_mi_be
    mi_be_synthese = mi_be_synthese * 32000 / np.max(np.abs(mi_be_synthese))  # normalise la sythese audio

    wavefile = wave.open('mi_be_synthese.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)

    for patate in mi_be_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())
    wavefile.close()
    return mi_be_synthese