# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:52:30 2022

@author: Lete
"""
import sympy
import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy.abc import x

xvals = np.linspace(0, 100, 1000)
f = x*sympy.sqrt(1+x**2)
g = 2*x**2
y1 = [f.evalf(subs={x:xval}) for xval in xvals]
y2 = [g.evalf(subs={x:xval}) for xval in xvals]
plt.plot(xvals[:100], y1[:100], 'r', xvals[:100], y2[:100], 'b')
plt.plot(xvals, y1, 'r', xvals, y2, 'b')

# 判定函数的阶（order)
print(sympy.O(f, (x, sympy.oo)))