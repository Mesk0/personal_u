# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:28:56 2022

@author: Lete
"""
import sympy
import matplotlib.pyplot as plt
import numpy as np
from math import *


x = range(1, 7)

factorial = [np.math.factorial(i) for i in x]
exponential = [np.e**i for i in x]
polynomial = [i**3 for i in x]
logarithmic = [np.log(i) for i in x]

plt.plot(x, factorial, 'black',
         x, exponential, 'blue',
         x, polynomial, 'green',
         x, logarithmic, 'red')


      