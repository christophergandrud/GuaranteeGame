#######################
# Containment Game
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 4 December 2012
#######################

# Import packages
import random
import pymc
import scipy as sp
import numpy as np
import math

#### Create proportion of recoverable assets to all assets ####
# True value
omega = random.uniform(0, 0.85)
print "omega: ", omega

# Expected value 
gammaHat = sp.mean(np.random.uniform(0, 0.85, 10000)) 
print "gammaHat: ", gammaHat

#### Create Two Signaler's Preferences (assume that they are symmetric)
# Set at +- half gammaHat 
# Signaler1 = gammaHat/2
# Signaler2 = -(gammaHat/2)

# Set Signaller 1 wants lower amount than Signaller 2
Signaler1 = 1
Signaler2 = 1

##### NOTE: We probably need to change the payoffs.  Signallers who want a
##### small cost will always share a Moderate PM's preferences Or assume that
##### issuing guarantees always has a cost, i.e. opportunity costs and interst
##### costs

# Find if omega falls within [gammaHat + 2*Signaler1, gammaHat + 2*Signaler1]
Upper = gammaHat + (2 * Signaler1)
Lower = gammaHat + (2 * Signaler2) 

print "Lower Bound: ", Lower
print "Upper Bound: ", Upper

if  Lower < omega < Upper:
	guarantee = gammaHat
else:
	guarantee = omega

print "Guarantee Decision: ", guarantee

Xreal = guarantee - omega

Upm = -(math.pow((0 - Xreal), 2))

print "PM's Utility: ", Upm


