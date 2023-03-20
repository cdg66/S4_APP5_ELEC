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
