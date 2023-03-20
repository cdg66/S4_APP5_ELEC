import wave
import struct
import numpy as np

def fct_generer_audio(audio_synthese, sample_rate):
    wavefile = wave.open('synthese_LA_guitare.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)

    for patate in audio_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())
       #wavefile.writeframes(struct.pack('h', np.int16(patate)))

    wavefile.close()

def fct_baathovenize(sol,mib,fa,re, sample_rate):
    wavefile = wave.open('la_5e_synthese_de_baathoven.wav', 'w')
    wavefile.setframerate(sample_rate)
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)
    audio_synthese = []
    audio_synthese = np.append(audio_synthese,[sol,sol,sol])
    audio_synthese = np.append(audio_synthese, mib)
    audio_synthese = np.append(audio_synthese, np.zeros(1000*10))
    audio_synthese = np.append(audio_synthese, [fa, fa, fa])
    audio_synthese = np.append(audio_synthese,re)
    for patate in audio_synthese:
        wavefile.writeframesraw(np.int16(patate).tobytes())
       #wavefile.writeframes(struct.pack('h', np.int16(patate)))

    wavefile.close()