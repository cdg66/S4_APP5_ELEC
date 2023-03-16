import wave

with wave.open('note_basson_plus_sinus_1000_Hz.wav', 'rb') as wav_file:
    # Get the sample rate of the file
    sample_rate = wav_file.getframerate()

    # Convertir les données audio en un tableau numpy
    audio_buffer = np.frombuffer(frames, dtype=np.int16)

    print("Sample rate: ", sample_rate)

with wave.open('note_guitare_LAd.wav', 'rb') as wav_file:
    # Get the sample rate of the file
    sample_rate = wav_file.getframerate()

    # Convertir les données audio en un tableau numpy
    audio_buffer = np.frombuffer(frames, dtype=np.int16)

    print("Sample rate: ", sample_rate)
