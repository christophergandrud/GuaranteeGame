#######################
# Game Test 2
# Christopher Gandrud
# 30 November 2012
#######################

# Import packages
import random
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

# Set at Signaller 1 public pays and signaller 2 Public pays 0
Signaler1 = -1
Signaler2 = 0

##### NOTE: We probably need to change the payoffs.  Signallers who want a
##### small cost will always share a Moderate PM's preferences Or assume that
##### issuing guarantees always has a cost, i.e. opportunity costs and interst
##### costs

# Find if omega falls within [gammaHat + 2*Signaler1, gammaHat + 2*Signaler1]
Upper = gammaHat + (2 * Signaler1)
Lower = gammaHat + (2 * Signaler2) 

print "Lower Bound: ", Lower
print "Upper Bound: ", Upper

if omega < Lower or omega > Upper:
	guarantee = gammaHat
elif omega >= Lower and omega <= Upper:
	guarantee = omega

print "Guarantee Decision: ", guarantee

Xreal = guarantee - omega

Upm = -(math.pow((0 - Xreal), 2))

print "PM's Utility: ", Upm


