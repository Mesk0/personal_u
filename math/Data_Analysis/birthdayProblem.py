# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:42:07 2022

@author: Lete
"""

import numpy as np
import matplotlib.pyplot as plt

def cal(x):
    global noshare, share, currentNoShare
    for i in range(x):
        new_factor = (365 - i)/365
        currentNoShare *= new_factor
        noshare[i+1] = currentNoShare
        share[i+1] = 1 - currentNoShare

noshare = {1: 0}
share = {1: 0}
currentNoShare = 1
cal(50)
print(noshare, share)

x1 = np.array([i+1 for i in noshare.keys()])
y1 = np.array([j for j in noshare.values()])
x2 = np.array([i+1 for i in share.keys()])
y2 = np.array([j for j in share.values()])
plt.scatter(x1, y1, s=10, color='red')
plt.scatter(x2, y2, s=10, color='blue')
plt.show()
