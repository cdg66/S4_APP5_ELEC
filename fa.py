import wave
import numpy as np
def fct_fa(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal):
#generation du fa
    x = np.arange(23000)
    note_fa = np.zeros(len(x))
    for i in range(33):
        note_fa += harmonique_amplitude[i] * np.sin(2 * np.pi * ((harmonique_frequence[i] / 1.06) * 0.794 / sample_rate) * x + harmonique_phase[i])

    fa_synthese = enveloppe[0:len(x)] * note_fa
    fa_synthese = fa_synthese * 32000 / np.max(np.abs(fa_synthese))  # normalise la sythese audio
    wavefile = wave.open('fa_synthese.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)

    for patate in fa_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())
    wavefile.close()
    return fa_synthese