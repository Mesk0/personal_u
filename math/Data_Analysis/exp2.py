# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:03:40 2022

@author: Lete
"""
import numpy as np

def exp2(x):
    sum = 0
    for k in range(100):
        sum += float(x**k)/np.math.factorial(k)
    return sum

print(exp2(2), exp2(3))