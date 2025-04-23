""" This script calculates a Short-Time Fourier Transform (STFT)
for a dipole moment time series output from Gaussian.

Written by:    J. J. Radler
Date Written:  07/03/17
Date Appended: 07/03/17

Input Arguments:	[1] Filename.log
					[2] (integer) window width (fs)
					[3] (integer) number of FFT bins per window
						(NOTE:  Cannot be < 1/2 (window width * 1000)

Outputs:			[1] Array of frequency spectra for
			    	the different time windows

"""

__author__ = 'joseph.radler'

import numpy as np
from numpy import linalg
import scipy as sp
from scipy import signal
import sys
from sys import argv

""" Input values for STFT """

D = np.loadtxt(sys.argv[1], 'float')	# array of all data
print "Dipole series matrix loaded"
mu_tot = np.array(D[: , 1], dtype=np.float32)	       # 1-D array of dipole moment
t = np.array(D[:, 0], dtype=np.float32)                  # 1-D array of time steps
Fs = np.float32(t[3] - t[2])			                	# Sampling rate (fs)
win_size = np.int32(np.ceil(np.int32(sys.argv[2]) / Fs))	  # Window size (points)
fft_size = np.int32(sys.argv[3])		      # FFT sample size (number of bins)

""" Note:  The fft_size determines the sampling rate (time-uncertainty).
Larger values will increase frequency resolution but decrease the time
resolution in the output spectrogram/waterfall plot. """

overlap = 0.1							# (1.0 - overlap) factor between windows

print "The length of mu_tot is %s" % len(mu_tot)
print "The length of t is %s" % len(t)
print "Time sampling for this series is %s" % Fs
print "The number of points per window is %s" % win_size
print "The number of sampled points in FFT is % s" % fft_size

skip_size = np.int32(np.floor(win_size * overlap))	  # Window translation size
pad_end_size = fft_size							         	# Zeros pad for fft
total_segs = np.int32(np.ceil(len(mu_tot) / skip_size))	# Total no. of segments
t_max = len(mu_tot) * Fs							 # Total time of simulation

print "The skip size is %s points" % skip_size
print "The max time of the simulation was %s fs" % t_max
print "The signal time-series is divided into %s segments" % total_segs

""" Now the STFT is calculated """

win = np.hanning(win_size) * overlap * 2
inner_pad = np.zeros((fft_size * 2) - win_size)

proc = np.concatenate((mu_tot, np.zeros(pad_end_size)))
out = np.empty((total_segs, fft_size), dtype = np.float32)

for k in xrange(total_segs):
	this_skip = skip_size * k
	seg = proc[this_skip : this_skip + win_size]
	windowed = seg #* win
	padded = np.append(windowed, inner_pad)
	spec = np.fft.fft(padded) / fft_size
	autopower = np.abs(spec * np.conj(spec))
	out[k, :] = autopower[:fft_size]

#AU_toEv = 27.2114	# Conversion factor from A.U. to eV
freq = np.fft.fftfreq(fft_size, d= (Fs * 41.3491)) * 2 * np.pi	# Recall that Fs is represented in 10^-15 seconds then converted to A.U.

np.savetxt('omega_list_%s_%s.txt' % (np.int32(np.floor((win_size + 1) * Fs)), fft_size), np.transpose(freq[:fft_size]), fmt='%.3f', newline = '\n')
np.savetxt('ehrenfest_spectrum_%s_%s.txt' % ((np.int32(np.floor(win_size + 1)*Fs)), fft_size), np.transpose(out),fmt='%.4E', delimiter=' ', newline='\n')
