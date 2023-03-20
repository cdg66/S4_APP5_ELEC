import wave
import numpy as np
def fct_sol(enveloppe,sample_rate,harmonique_amplitude,harmonique_frequence,harmonique_phase,fft_signal):
    #generation du sol
    x = np.arange(160000)
    note_sol = np.zeros(len(fft_signal))
    for i in range(33):
        note_sol += harmonique_amplitude[i] * np.sin(2 * np.pi * ((harmonique_frequence[i]/1.06)*0.891 / sample_rate) * x + harmonique_phase[i])

    sol_synthese = enveloppe * note_sol
    sol_synthese = sol_synthese * 32000 / np.max(np.abs(sol_synthese))  # normalise la sythese audio

    wavefile = wave.open('sol_synthese.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)

    for patate in sol_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())


    wavefile.close()
