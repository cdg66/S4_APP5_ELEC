from DFT import *
import scipy

with wave.open('note_basson_plus_sinus_1000_Hz.wav', 'rb') as wav_file:
    # nb d'échantillon du fichier
    num_frames = wav_file.getnframes()

    # Retourne la fréquence d'échantillonage en Hz
    sample_rate = wav_file.getframerate()

    # lit tout le contenu du fichier et stock les amplitudes dans frames
    frames = wav_file.readframes(num_frames)

    # Convertir les échantillons audio en une série temporelle de valeurs d'amplitude
    signal = np.frombuffer(frames, dtype=np.int16)

    #freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies, fft_signal = fct_DFT(
    #    signal, sample_rate)
    # graphique du FFT du signal
    x = np.arange(num_frames)
    plt.plot(x, signal)
    plt.title('Signal audio originale')
    plt.xlabel('temps')
    plt.ylabel('Amplitude')
    plt.show()
    #calculate FFT of signal
    signalFFT = np.fft.fft(signal)
    plt.plot(x, np.abs(signalFFT))
    plt.title('Signal audio originale en fft')
    plt.xlabel('Fréquence')
    plt.ylabel('Amplitude')
    plt.show()
    range = np.arange(3001, 3123, 1)
    for i in range:
        signalFFT[i] = 0 + -1000j
        signalFFT[135051-i] = 0 + -1000j
    plt.plot(x, np.abs(signalFFT))
    plt.title('Signal audio originale en fft')
    plt.xlabel('Fréquence')
    plt.ylabel('Amplitude')
    plt.show()
    newsignal = np.fft.ifft(signalFFT)
    plt.plot(x, signal)
    plt.title('Signal audio nouveau')
    plt.xlabel('temps')
    plt.ylabel('Amplitude')
    plt.show()
    newsignal = np.fft.fft(newsignal)
    plt.plot(x, signal)
    plt.title('Signal audio nouveau')
    plt.xlabel('temps')
    plt.ylabel('Amplitude')
    plt.show()
    #remove 1K

    #reverseFFT