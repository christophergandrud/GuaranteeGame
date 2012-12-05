#######################
# Containment Game: 1 Signaller
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 5 December 2012
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math as m
import pandas

b = 0.24

nFloat = m.ceil(-0.5 + 0.5 * m.pow((1 + 2/b), 0.5))

N = int(nFloat)

print 'N: ', N

a1 = (1 - 2 * N * (N - 1) * b)/N

print 'a1: ', a1

Nless1 = N - 1

for i in range(2, Nless1 + 1 ):
	a = a1 * i + (2 * i) * (i - 1) * b
	print 'a', i, a  
