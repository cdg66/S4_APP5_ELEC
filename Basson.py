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
    plt.xlabel('Fréquence')
    plt.ylabel('Amplitude')
    plt.show()

    #Calcul du filtre Passe-Bas
    Fe = sample_rate # 44100
    w = np.pi * 2 * Fe

    N = 1024
    Nm1 = N-1
    FcL = 980
    FcH = 1020
    FcLP = (FcH-FcL)/2
    w0 = 2 * np.pi * 1000
    mc = (FcLP/Fe)*N #0.46439909297052157
    mc = 1
    K = mc*2+1
    print(mc)
    # generatre filter in the frequency domain
    filter = np.zeros(N)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    filter[0] = 1
    filter[1] = 1
    #filter[2] = 0.5
    filter[N-1] = 1
    #filter[N - 2] = 0.5
    x = np.arange(N)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.plot(x, filter)
    # inverse FFt to get the filter in the time domain
    #filter = np.real(np.fft.fftshift(np.fft.ifft(filter)))
    filter = np.fft.ifft(filter)
    #x = np.arange(-N / 2, N / 2)
    ax2.plot(x, filter)
    #

    # Convert it to a band reject filter
    # dirac = np.zeros(N) #create dirac
    # dirac[0] = 1
    #
    # for n in range(len(filter)):
    #
    #     #filter[n] = filter[n] * currentcos
    #     filter[n] = dirac[n] - 2*filter[n] * np.cos(w0 * x[n])
    # print(filter)
    # ax3.plot(x, filter)
    # plt.show()
    # plt.plot(x, filter)
    # plt.title('Filter offsetted')
    #
    # plt.xlabel('Fréquence')
    # plt.ylabel('Amplitude')
    # plt.show()
    #convoluate singal and filter together
    newsignal = scipy.signal.convolve(filter,signal, mode='full')

    #     #fft the band reject filter and signal
    # filter = np.fft.fft(filter)
    # signalFFT = np.fft.fft(signal)
    #     #multiply both of them
    # signalfiltered = signalFFT * filter
    #     #reverse fft of the mupltiplication
    # signalfiltered = np.fft.ifft(signal)
    fig2, (axb1, axb2) = plt.subplots(2, 1)
    x = range(len(newsignal))
    axb1.plot(x, newsignal)
    x = range(len(signal))
    axb2.plot(x, signal)
    plt.title('old singal')

    plt.xlabel('time')
    plt.ylabel('Amplitude')
    plt.show()
    #save as a wave file
wave_file = wave.open("note_basson_minus_sinus_1000_Hz.wav", "w")
wave_file.setnchannels(1) # Mono
wave_file.setsampwidth(16// 8) # Sample width in bytes
wave_file.setframerate(sample_rate) # Sample rate in Hz
# Write waveform data to wave file
wave_file.writeframes(newsignal)
# Close wave file
wave_file.close()

