# PYTHON SCRIPT FOR PARSING LINES OF DELIMITED TEXT
# FOR NUCLEAR COORDINATES TO CALCULATE THE INTERATOMIC
# DISTANCE.
#
# BY: JOSEPH J. RADLER
# WRITTEN: 6/7/17
# APPENDED: 6/8/17
#

import numpy as np
from numpy import linalg
import sys
from sys import argv

arg = sys.argv[1]
coords = np.loadtxt(arg, 'float')
d = []  # Output value array
k = 0	# Iteration index for input array line

while k < len(coords):
	v = coords[k, :]
	w = coords[k + 1, :]
        dist = np.linalg.norm(w - v)
	d.append(dist)
	k = k + 2
	
np.savetxt('distance.txt', d, delimiter='\n')


	

