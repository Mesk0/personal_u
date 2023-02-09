# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:43:54 2022

@author: Lete
"""
import matplotlib.pyplot as plt
import numpy as np
from math import *

f = lambda x: x**2-2*x-6
x = np.linspace(0, 5, 100)
y = f(x)

plt.plot(x, y, 'red')
plt.grid('off')

I = plt.axhline(-8, 0, 1, linewidth = 2, color = 'black')
I = plt.axvline(0, 0, 1, linewidth = 2, color = 'black')

I = plt.axhline(y = 2, xmin = 0, xmax = 0.8, linestyle = '--')
I = plt.axvline(x = 4, ymin = 0, ymax = float(5)/9, linestyle = '--')

I = plt.axhline(-6, 3.7/5, 4.3/5, linewidth = 2, color = 'black')
I = plt.axvline(1, 6.0/18, 14.0/18, linewidth = 2, color = 'black')

p = plt.axhspan(-2, 6, 0, (1+sqrt(13))/15, alpha = 0.15, ec = 'none')
p = plt.axvspan((1+sqrt(5)), (1+sqrt(13)), 0, 1.0/3, alpha = 0.15, ec = 'none')

p = plt.axhspan(f(3.7), f(4.3), 0, 4.3/5, alpha = 0.3, ec = 'none')
p = plt.axvspan(3.7, 4.3, 0, (f(3.7)+8)/18, alpha = 0.3, ec = 'none')

plt.axis([0, 5, -8, 10])

plt.text(0.8,-1,r"$\epsilon$", fontsize = 18)
plt.text(0.8,4,r"$\epsilon$", fontsize = 18)
plt.text(3.75,-7.0,r"$\delta$", fontsize = 18)
plt.text(4.1,-7.0,r"$\delta$", fontsize = 18)
plt.text(3.95,-7.0,r"$a$", fontsize = 18)
plt.text(4.5,8.5,r"$f(x)$", fontsize = 18, color = "red")

plt.show()
