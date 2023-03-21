import numpy as np
import matplotlib.pyplot as plt
def fct_enveloppe(signal, sample_rate, som_32_harmoniques, N):
       abs_signal = abs(signal)
       #fc = np.pi/1000
       fe =sample_rate
       fc = (np.pi / 1000) * fe / (2 * np.pi)
       m = (fc * N) / fe
       #print(m)
       K = 2 * m + 1
       print(K)
       k = np.arange(-N / 2, N / 2, 1)
       print(k)
       Hk = np.zeros(N)
       pos = np.linspace(-(N / 2) + 1, N / 2, N)
       index = np.arange(0, N, 1)
       d = np.zeros(N)  # dirac
       d[512] = 1
       for i in range(len(Hk)):
              if k[i] != 0:
                     Hk[i] = (1 / N) * (np.sin((np.pi * k[i] * K) / N) / np.sin((np.pi * k[i]) / N))
              else:
                     Hk[i] = K / N  # or any other value you want to assign when denominator is zero
       envelope = np.convolve(abs_signal, Hk, mode='same')
       audio_synthese = envelope * som_32_harmoniques
       audio_synthese = audio_synthese * 32000 / np.max(np.abs(audio_synthese))
       Hm = np.fft.fft(Hk)
       x_freqs = np.fft.fftfreq(len(Hm), d=1 / fe)
       plt.plot(x_freqs[:300], 20 * np.log10(np.abs(Hm[:300])))
       #plt.plot(x_freqs[:300], np.abs(Hm[:300]))
       plt.title("Basse-bas dans le domaine des fréquences")
       plt.xlabel('Fréquences')
       plt.ylabel('Amplitude(dB)')
       plt.show()

       return envelope,audio_synthese



