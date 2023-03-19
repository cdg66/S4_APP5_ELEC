from DFT import *
import struct
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

    params = wav_file.getparams()

#freq_fundamental, fundamental_amplitude, harmonic_amplitude, harmonic_phases, harmonic_frequencies, fft_signal = fct_DFT(
#    signal, sample_rate)
# graphique du FFT du signal
x = np.arange(num_frames)
plt.plot(x, signal)
plt.title('Signal audio originale')
plt.xlabel('Fréquence')
plt.ylabel('Amplitude')
plt.show()

#calculate lowpassfilter
N = 1024
fe = sample_rate
f0 = 1000
f1 = 980
f2 = 1020
fc = (1020-980)/2
print(fc)
m = (fc*N)/fe # what it truly is
#m = 1 # what we aproximate at
print(m)
K = 2 * m + 1
print(K)
k = np.arange(-N/2,N/2,1)
print(k)
Hk = np.zeros(N)
pos = np.linspace(-(N / 2) + 1, N / 2, N)
index = np.arange(0,N,1)
d = np.zeros(N) #dirac
d[512] = 1
for i in range(len(Hk)):
    #denominator = np.sin((np.pi * k[i]) / N)
    if k[i] != 0:
        Hk[i] = (1/N)*(np.sin((np.pi * k[i]* K)/N )/np.sin((np.pi * k[i])/N ))
    else:
        Hk[i] = K/N  # or any other value you want to assign when denominator is zero
print(Hk)
plt.plot(pos,Hk)
plt.title("Hk lowpass")
plt.xlabel('temps')
plt.ylabel('Amplitude')
plt.show()




#convert to a bandreject filter

print(d)
    #calculate w0
w0 = 2*np.pi*f0/fe
    #evaluate to the new formula

for i in range(0,N,1):
    Hk[i] = d[i] - np.multiply(2 * Hk[i], np.cos(w0 * k[i]))
    #Hk[i] = d[i] - 2*Hk[i] * np.cos(w0*k[i])
plt.plot(pos,Hk)
plt.title("Hk band reject")
plt.xlabel('temps')
plt.ylabel('Amplitude')
plt.show()

Hm = np.fft.fft(Hk)
cb_freqs = np.fft.fftfreq(len(Hm), d=1 / fe)
plt.plot(cb_freqs[:500], 20 * np.log10(np.abs(Hm[:500])))
plt.title("Hk band reject in frequency domain")
plt.xlabel('Fréquence')
plt.ylabel('Amplitude(dB)')
plt.show()

#convoluate

SigFiltered = np.convolve(signal,Hk)
SigFiltered = np.convolve(signal,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
plt.plot(SigFiltered)
plt.title("Hk band reject in frequency domain")
plt.xlabel('Fréquence')
plt.ylabel('Amplitude(dB)')
plt.show()
#save to a .wave file
with wave.open("note_basson_minus_sinus_1000_Hz.wav","wb") as write:
    write.setparams(params)
    waveform_data = np.zeros(len(SigFiltered))
    #write.writeframes(SigFiltered.tobytes())
    for sample in SigFiltered:
        write.writeframes(struct.pack('h', np.int16(sample)))



