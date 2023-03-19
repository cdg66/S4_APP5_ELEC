import wave
import numpy as np
import matplotlib.pyplot as plt
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
    return num_frames, sample_rate, frames, signal