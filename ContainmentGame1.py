#######################
# Containment Game
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 4 December 2012
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math
import pandas

# Initialize Lists
OmegaL = []
UpmL = []
Signaler1L = []
Signaler2L = []

#### Create Two Signaler's Preferences (assume that they are symmetric)
# Set at +- half gammaHat 
# Signaler1 = gammaHat/2
# Signaler2 = -(gammaHat/2)

# Set Signaller 1 wants lower amount than Signaller 2
Signaler1 = -0.1
Signaler2 = 0.1

#### Create proportion of recoverable assets to all assets ####
# True value
OmegaRange = np.random.uniform(0, 0.85, 1000) 

for omega in OmegaRange:

	# Expected value 
	gammaHat = sp.mean(np.random.uniform(0, 0.85, 10000)) 

	# Find if omega falls within [gammaHat + 2*Signaler1, gammaHat + 2*Signaler1]
	Lower = gammaHat + (2 * Signaler1)
	Upper = gammaHat + (2 * Signaler2) 

	if  Lower < omega < Upper:
		guarantee = gammaHat
	else:
		guarantee = omega

	# Find PM's utility

	Xreal = guarantee - omega

	Upm = -(math.pow((0 - Xreal), 2))

	# Append to lists

	OmegaL.append(omega)
	UpmL.append(Upm)
	Signaler1L.append(Signaler1)
	Signaler2L.append(Signaler2)

d = {'Omega': OmegaL,
	'Upm' : UpmL,
	'Signaler1' : Signaler1L,
	'Signaler2' : Signaler2L
	}

# Create data frame
OutputData = pandas.DataFrame(d)

OutputData.to_csv('/git_repositories/ContainmentGame/SimulatedData/Test.csv')


