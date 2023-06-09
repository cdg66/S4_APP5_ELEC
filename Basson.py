import numpy as np
import wave
import matplotlib.pyplot as plt

import struct
import scipy
from scipy.signal import find_peaks

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


#calculate lowpassfilter
N = 1024
fe = sample_rate
f0 = 1000
f1 = 980
f2 = 1020
fc = (1020-980)/2
print(fc)
m = (fc*N)/fe
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

    if k[i] != 0:
        Hk[i] = (1/N)*(np.sin((np.pi * k[i]* K)/N )/np.sin((np.pi * k[i])/N ))
    else:
        Hk[i] = K/N  # or any other value you want to assign when denominator is zero
print(Hk)

han = np.hanning(len(Hk))
Hk = han * Hk

plt.plot(pos,Hk)
plt.title("Hk lowpass")
plt.xlabel('temps')
plt.ylabel('Amplitude')
plt.show()


# han = np.hanning(len(Hk))
# Hk = han * Hk


#convert to a bandreject filter

print(d)
    #calculate w0
w0 = 2*np.pi*f0/fe
    #evaluate to the new formula

for i in range(0,N,1):
    Hk[i] = d[i] - np.multiply(2 * Hk[i], np.cos(w0 * k[i]))

plt.plot(pos,Hk)
plt.title("Hk band reject")
plt.xlabel('temps')
plt.ylabel('Amplitude')
plt.show()

Hm = np.fft.fft(Hk)
x_freqs = np.fft.fftfreq(len(Hm), d=1 / fe)
plt.plot(x_freqs[:300], 20 * np.log10(np.abs(Hm[:300])))
plt.title("Hk band reject in frequency domain")
plt.xlabel('Fréquence')
plt.ylabel('Amplitude(dB)')
plt.show()
#calculate the response of a sinusoid at a frequency of 1000Hz
# Generate time samples
num_samples = 1 * fe
sinus_time = np.linspace(0, 1, num_samples, endpoint=False)
sinus = np.sin(2 * f0 * np.pi  *sinus_time)
sinus_filtered = np.convolve(sinus,Hk)
sinus_FFT = np.fft.fft(sinus)
sin_X_FFT = np.fft.fftfreq(len(sinus_FFT), d=1/fe)
sinus_filtered_FFT = np.fft.fft(sinus_filtered)
sin_filtered_X_FFT = np.fft.fftfreq(len(sinus_filtered_FFT), d=1/fe)
plt.plot(sinus[0:2500])
plt.xlabel("Échantillon")
plt.ylabel("Amplitude")
plt.show()
plt.plot(sinus_filtered[0:2500])
plt.xlabel("Échantillon")
plt.ylabel("Amplitude")
plt.show()

plt.plot(sin_filtered_X_FFT[511:5000] , 20*np.log10(np.abs(sinus_filtered[0:len(sin_filtered_X_FFT[511:5000])])))
plt.plot(sin_filtered_X_FFT[511:5000], np.angle(sinus_filtered[0:len(sin_filtered_X_FFT[511:5000])]))
plt.xlabel("Échantillon")
plt.ylabel("Amplitude")
plt.show()
plt.plot(sinus_filtered)
plt.xlabel("Échantillon")
plt.ylabel("Amplitude")


#convoluate

SigFiltered = np.convolve(signal,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
SigFiltered = np.convolve(SigFiltered,Hk)
fft_sign_filtered = np.fft.fft(SigFiltered)

mag_fft_signal = np.abs(fft_sign_filtered)
phase_fft_signal = np.angle(fft_sign_filtered)
freq= np.fft.fftfreq(len(fft_sign_filtered), d=1/fe)
index, _ = find_peaks(mag_fft_signal,900000)
index = index[73]
# on trouve les harmoniques ici
n = 32
harmonique_frequence = [0] * n
harmonique_amplitude = [0] * n
harmonique_phase = [0] * n

for i in range(1, n):
    harmonique_frequence[i-1] = freq[index*i]
    harmonique_amplitude[i-1] = mag_fft_signal[index*i]
    harmonique_phase[i-1] = phase_fft_signal[index*i]
    print(
        f"Harmoniques {i-1} Frequency: {harmonique_frequence[i-1]:.2f} Hz, Amplitude: {harmonique_amplitude[i-1]:.2f},"f" module_phase: {harmonique_phase[i-1]:.2f} radians")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.stem(harmonique_frequence, harmonique_amplitude)
ax1.set_title('Modules des harmoniques', fontsize=18)
ax1.set_yscale('log')
ax1.set_xlabel("Fréquences en Hz", fontsize=16)
ax1.set_ylabel("Amplitude", fontsize=16)
ax1.tick_params(axis='both', which='major', labelsize=16, width=2)

ax2.stem(harmonique_frequence, harmonique_phase)
ax2.set_xlabel("Phases en rad", fontsize=16)
ax2.set_title('Phases des harmoniques', fontsize=18)
ax2.set_ylabel("Amplitude", fontsize=16)
ax2.tick_params(axis='both', which='major', labelsize=16, width=2)

plt.tight_layout()
plt.show()

# somme 32 harmoniques
# x = np.arange(160000)
# som_32_harmoniques = np.zeros(len(fft_sign_filtered))
# for i in range(33):
#     som_32_harmoniques += harmonique_amplitude[i] * np.sin(
#         2 * np.pi * (harmonique_frequence[i] / sample_rate) * x + harmonique_phase[i])
fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True)
ax1.plot(x, signal)
ax1.set_title('Signal audio originale')
ax1.set_xlabel('Fréquence')
ax1.set_ylabel('Amplitude')
ax2.plot(SigFiltered)
ax2.set_title("signal passe dans le filtre 5 fois")
ax2.set_xlabel('Amplitudes')
ax2.set_ylabel('time(samples)')
plt.show()

fig2, (ax3, ax4) = plt.subplots(2, 1,  sharey=True)
xFFT = np.fft.fftfreq(len(np.fft.fft(signal)), d=1/fe)
sFFT = np.fft.fft(signal)
ax3.plot(xFFT[511:5000], 20*np.log10(abs(sFFT[511:5000])))
ax3.set_title('Signal audio originale in the frequency domain')
ax3.set_xlabel('Fréquence')
ax3.set_ylabel('Amplitude(dB)')
xfFFT = np.fft.fftfreq(len(np.fft.fft(SigFiltered)), d=1/fe)
sfFFT = np.fft.fft(SigFiltered)
ax4.plot(xfFFT[511:5000], 20*np.log10(abs(sfFFT[511:5000])))
ax4.set_title("signal filtered in the frequency domain")
ax4.set_xlabel('Fréquence')
ax4.set_ylabel('Amplitude(dB)')
plt.show()
fig2, (ax5, ax6) = plt.subplots(2, 1,  sharey=True)
ax5.plot(xFFT[511:5000], np.angle(sFFT[511:5000], deg=False))
ax5.set_title('Angle du signal original')
ax5.set_xlabel('Fréquence')
ax5.set_ylabel('Amplitude(rad)')
xfFFT = np.fft.fftfreq(len(np.fft.fft(SigFiltered)), d=1/fe)
sfFFT = np.fft.fft(SigFiltered)
ax6.plot(xfFFT[511:5000], np.angle(sfFFT[511:5000], deg=False))
ax6.set_title("angle du signal filtree")
ax6.set_xlabel('Fréquence')
ax6.set_ylabel('Amplitude(rad)')
plt.show()
#save to a .wave file
with wave.open("note_basson_minus_sinus_1000_Hz.wav","wb") as write:
    write.setparams(params)
    waveform_data = np.zeros(len(SigFiltered))
    for sample in SigFiltered:
        write.writeframes(struct.pack('h', np.int16(sample)))




