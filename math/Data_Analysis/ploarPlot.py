# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:55:29 2022

@author: Lete
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import sympy

x = np.linspace(-np.pi, np.pi)
lhs = e**(1j*x)
rhs = cos(x) + 1j*sin(x)
print(sum(lhs == rhs) == len(x))
z = sympy.Symbol('z', real = True)
sympy.expand(sympy.E**(sympy.I*z), conplex = True)

for p in e**(1j*x):
    plt.polar([0, angle(p)],[0, abs(p)], marker='o')
plt.show()