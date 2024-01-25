import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import windows

data = np.loadtxt('csv/sine_200hz.csv', delimiter=',')
signal = data[5:, 0]  
sampling_rate = 31250/5  

window = windows.hann(len(signal))
signal_windowed = signal * window

n_padded = 2**np.ceil(np.log2(len(signal_windowed)))
signal_padded = np.pad(signal_windowed, (0, int(n_padded - len(signal_windowed))), 'constant')

fft_result = np.fft.fft(signal_padded)
fft_freq = np.fft.fftfreq(len(signal_padded), 1/sampling_rate)
fft_magnitude = np.abs(fft_result)

# Anta at din kjente signal-frekvens er 200 Hz
signal_freq = 200
signal_idx = np.argmax(fft_freq == signal_freq)
signal_amplitude = fft_magnitude[signal_idx]

# Beregn støynivå (kan tilpasses etter ditt behov)
noise_level = np.mean(fft_magnitude[fft_freq > signal_freq + 50])  # Støy utenfor signalområdet

# Beregn SNR
snr = 20 * np.log10(signal_amplitude / noise_level)
print("SNR: ", snr, "dB")


plt.figure(figsize=(10, 6))
plt.plot(fft_freq, np.abs(fft_result))
plt.title("Frekvensspektrum")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
