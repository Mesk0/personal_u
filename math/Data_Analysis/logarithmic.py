# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:14:57 2022

@author: Lete
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100, endpoint = False)
y1 = np.log2(x)
y2 = np.log(x)
y3 = np.log10(x)

plt.plot(x, y1, 'red', x, y2, 'yellow', x, y3, 'blue')
plt.show()