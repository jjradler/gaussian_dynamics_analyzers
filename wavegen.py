# Wavegen creates a list of integers scaled by some scalar value

m = 50000	#number of integer increments (steps in job 0.0012 fs)
s = 0.068925	#scaled value (eV/step) in Fourier space

for x in range(0, m+1):
	print x, x*s
