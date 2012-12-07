#######################
# Containment Game: 1 Signaller
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 5 December 2012
# Based on Crawford and Sobel (1982)
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math as m
import pandas

# True value
OmegaRange = np.random.uniform(0, 1, 1000) 

# Set difference between PM and Signaler
bRange = [0.001, 0.05, 0.1, 0.25]

omegaMax = 1

# Find cut points 
a0 = 0
aN = 1

a = {}

for omega in OmegaRange:
	for b in bRange:
		# Find the number of cut points
		nFloat = m.ceil(-0.5 + 0.5 * m.pow((omegaMax + 2/b), 0.5))
		N = int(nFloat)
		print 'N: ', N

		# Find a1 cut point
		a1 = (omegaMax - 2 * N * (N - omegaMax) * b)/N

		print 'a1: ', a1

		Nless1 = N - 1

		for i in range(2, Nless1 + 1):
			key = i
			a[key] = a1 * i + (2 * i) * (i - omegaMax) * b
			print 'a:', i, a[key]  



