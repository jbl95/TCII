#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:53:08 2021

@author: jbl
"""

from splane import pzmap, grpDelay, bodePlot
from scipy.signal import TransferFunction,bode
import matplotlib.pyplot as plt
import numpy as npy

## Simulación matemática.

C1 = 238e-12
C2 = 2.4e-9
C3 = 24e-9
R3 = 4700
G3 = 1 / R3
gm1 = 2.13e-6
gm2 = 21.3e-6
gm3 = 212.8e-6

c = (gm2 / C2) + (G3 / C3)
b = ((gm1*gm2) / (C1*C2)) + ((gm2*G3) / (C2*C3))
a = ((gm1*gm2*G3) / (C1*C2*C3))
d = ((gm1*gm2*gm3) / (C1*C2*C3))

num = [d]
den = [1,c,b,a]
 
my_tf = TransferFunction( num, den )

## Ploteo.
bodePlot(my_tf)
pzmap(my_tf)