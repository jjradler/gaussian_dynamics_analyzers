import numpy as np
import sys
from sys import argv

"""
This performs an elementwise sum of the three components of the dipole
moment time series from Singlet Ehrenfest dynamics simulatious in Gaussian in
a VERY crappy, hacky way. But it'll do the trick for now.

The order of input arguments is:
[1] mu_x
[2] mu_y
[3] mu_z

Output argument is a total fft of the dipole moment time series.
Hope it works. -J. R.
"""

ftmu_x = np.loadtxt(sys.argv[1], 'float')
ftmu_y = np.loadtxt(sys.argv[2], 'float')
ftmu_z = np.loadtxt(sys.argv[3], 'float')

ftmu_tot = np.array(ftmu_x, dtype=np.float32) + np.array(ftmu_y, dtype=np.float32) + np.array(ftmu_z, dtype=np.float32)

np.savetxt('ehrenfest_spectrum_total.txt', ftmu_tot, fmt='%.4E', delimiter=' ', newline='\n')
