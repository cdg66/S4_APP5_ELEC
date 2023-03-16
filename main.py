import wave
import numpy as np
import matplotlib.pyplot as plt

with wave.open('note_basson_plus_sinus_1000_Hz.wav', 'rb') as wav_file:
    # Get the number of frames in the file
    num_frames = wav_file.getnframes()

    # Get the sample rate of the file
    sample_rate = wav_file.getframerate()

    # Get the duration of the file
    duration = num_frames / float(sample_rate)

    # Read all the frames from the file
    frames = wav_file.readframes(num_frames)

    # Convertir les données audio en un tableau numpy
    audio_buffer = np.frombuffer(frames, dtype=np.int16)

    print("Sample rate: ", sample_rate)


    

with wave.open('note_guitare_LAd.wav', 'rb') as wav_file:
    # Get the number of frames in the file
    num_frames = wav_file.getnframes()

    # Get the sample rate of the file
    sample_rate = wav_file.getframerate()

    # Get the duration of the file
    duration = num_frames / float(sample_rate)

    # Read all the frames from the file
    frames = wav_file.readframes(num_frames)

    # Convertir les données audio en un tableau numpy
    audio_buffer = np.frombuffer(frames, dtype=np.int16)

    print("Sample rate: ", sample_rate)
