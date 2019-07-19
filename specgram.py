from plot_raw import load
import sys, numpy as np

strain_H1, strain_L1, time, event = load(sys.argv[2], "GW150914")
tevent = event['tevent']
fs = event['fs']

deltat = 5 # 时间窗
# index into the strain time series for this time interval:
indxt = np.where((time >= tevent-deltat) & (time < tevent+deltat))

eventname = event['name']

# pick a shorter FTT time interval, like 1/8 of a second:
NFFT = int(fs/8)
# and with a lot of overlap, to resolve short-time features:
NOVL = int(NFFT*15./16)

# and choose a window that minimizes "spectral leakage"
# (https://en.wikipedia.org/wiki/Spectral_leakage)
window = np.blackman(NFFT)

spec_cmap='ocean'

import matplotlib as mpl
mpl.use("Agg")
from matplotlib import pyplot as plt

# Plot the H1 spectrogram:
plt.figure(figsize=(10,6))
spec_H1, freqs, bins, im = plt.specgram(strain_H1[indxt], NFFT=NFFT, Fs=fs, window=window, 
                                        noverlap=NOVL, cmap=spec_cmap, xextent=[-deltat,deltat])

plt.xlabel('time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar()
plt.axis([-deltat, deltat, 0, 2000])
plt.title('aLIGO H1 strain data near '+eventname)
plt.savefig(sys.argv[1])

# Plot the L1 spectrogram:
# plt.figure(figsize=(10,6))
# spec_H1, freqs, bins, im = plt.specgram(strain_L1[indxt], NFFT=NFFT, Fs=fs, window=window, 
#                                         noverlap=NOVL, cmap=spec_cmap, xextent=[-deltat,deltat])
# plt.xlabel('time (s) since '+str(tevent))
# plt.ylabel('Frequency (Hz)')
# plt.colorbar()
# plt.axis([-deltat, deltat, 0, 2000])
# plt.title('aLIGO L1 strain data near '+eventname)
# plt.savefig(eventname+'_L1_spectrogram.png')
