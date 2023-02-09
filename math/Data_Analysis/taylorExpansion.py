# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:25:07 2022

@author: Lete
"""
import matplotlib.pyplot as plt
import sympy
import numpy as np
from sympy import *
from math import e

def taylorExpansion(func,var,expPoint,numTerms):
        return func.series(var,expPoint,numTerms)
    
def polyApprox(func, num_terms):
    sums = 0
    for i in range(num_terms):
        numerator = func.diff(x, i)
        numerator = numerator.evalf(subs = {x:0})
        denominator = np.math.factorial(i)
        sums += numerator/denominator*x**i
    return sums
        
x = sympy.Symbol('x')
exp = e**x

sum5 = polyApprox(exp, 5)
sum10 = polyApprox(exp, 10)
sum15 = exp.series(x, 0, 15).removeO()

xvals = np.linspace(5, 10, 100)

for xval in xvals:
    plt.plot(xval, exp.evalf(subs={x:xval}), 'bo',
             xval, sum5.evalf(subs={x:xval}), 'ro',
             xval, sum10.evalf(subs={x:xval}), 'go',
             xval, sum15.evalf(subs={x:xval}), 'yo')
