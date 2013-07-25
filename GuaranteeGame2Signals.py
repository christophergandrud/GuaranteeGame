#######################
# Guarantee Game: 2 Signallers
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 25 July 2013
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math
import pandas

# Initialize Lists
omegaL = []
GuaranteeL = []
UpmL = []
Us1L = []
Us2L = []
Signaler1L = []
Signaler2L = []

#### Create proportion of recoverable assets to all assets ####
# True value
omegaRange = np.random.uniform(0.65, 0.95, 1000) 

# Set Signaller 1 wants lower amount than Signaller 2
S1Range = [-0.05, -0.15]
S2Range = [0.05, 0.15]

for omega in omegaRange:
	for S1 in S1Range:
		for S2 in S2Range:

			# Expected value 
			gammaHat = sp.mean(np.random.uniform(0.65, 0.95, 100000)) 

			# Find if omega falls within 
			# [gammaHat + 2*Signaler1, gammaHat + 2*Signaler2]
			Lower = gammaHat + (2 * S1)
			Upper = gammaHat + (2 * S2) 

			if  Lower < omega < Upper:
				guarantee = gammaHat
			else:
				guarantee = omega

			# Find utilities

			Xreal = guarantee - omega

			Upm = -(math.pow((0 - Xreal), 2))

			Us1 = -(math.pow((S1 - Xreal), 2))
			Us2 = -(math.pow((S2 - Xreal), 2))

			# Append to lists

			omegaL.append(omega)
			GuaranteeL.append(guarantee)
			UpmL.append(Upm)
			Us1L.append(Us1)
			Us2L.append(Us2)
			Signaler1L.append(S1)
			Signaler2L.append(S2)

d = {'omega' : omegaL,
	'Guarantee' : GuaranteeL,
	'Upm' : UpmL,
	'Us1' : Us1L,
	'Us2' : Us2L,
	'Signaler1' : Signaler1L,
	'Signaler2' : Signaler2L
	}

# Create data frame
OutputData = pandas.DataFrame(d)

OutputData.to_csv('/git_repositories/GuaranteeGame/SimulatedData/SimData09.csv')


