import matplotlib as mpl
mpl.use("Agg")
from matplotlib import pyplot as plt

from plot_raw import load
import sys, numpy as np

strain_H1, strain_L1, time, event = load(sys.argv[2], "GW150914")

fs = event['fs'] # 4096Hz by default
N = len(strain_H1)
dt = 1.0 / fs

kH1 = np.abs(np.fft.rfft(strain_H1)) * 2/N
kL1 = np.abs(np.fft.rfft(strain_L1)) * 2/N
freq = np.fft.rfftfreq(N, dt)

plt.figure(figsize = (10,7))
plt.loglog(freq, kH1, label="H1")
plt.loglog(freq, kL1, label="L1")
plt.legend()

plt.xlim(20, 2000)
plt.xlabel('frequency [Hz]')
plt.grid()
plt.savefig(sys.argv[1])
