import json, sys

events = json.load(open(sys.argv[2], "r"))
event = events['GW150914']

import readligo as rl

fn_H1 = "data/" + event['fn_H1']
strain_H1, time, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
fn_L1 = "data/" + event['fn_L1']
strain_L1, time, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')

tevent = event['tevent'] - time[0]
# Time since 9:50:29 GMT 2015
time = time - time[0]
# Sampling rate
fs = event['fs']

import matplotlib as mpl
mpl.use("Agg")

import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
plt.plot(time, strain_H1, label="H1")
plt.plot(time, strain_L1, label="L1")
plt.vlines((16,), ymin=-2e-18, ymax=1e-18)
plt.title("Strains of 2 detectors")
plt.xlabel('time since Sep 14 9:50:29 GMT 2015 [s]');
plt.ylabel('strain')
plt.grid('on')
plt.legend()
plt.savefig(sys.argv[1])
