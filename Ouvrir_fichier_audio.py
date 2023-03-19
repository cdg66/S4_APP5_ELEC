import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
def parametre_fichier_audio() :
    with wave.open('note_guitare_LAd.wav', 'rb') as wav_file:
        # nb d'échantillon du fichier
        num_frames = wav_file.getnframes()

        # Retourne la fréquence d'échantillonage en Hz
        sample_rate = wav_file.getframerate()

        # lit tout le contenu du fichier et stock les amplitudes dans frames
        frames = wav_file.readframes(num_frames)

        #Convertir les échantillons audio en une série temporelle de valeurs d'amplitude
        signal = np.frombuffer(frames, dtype=np.int16)

    sample_rate, signal = wavfile.read('note_guitare_LAd.wav')
    return signal, sample_rate, num_frames