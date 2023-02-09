# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:26:36 2022

@author: Lete
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x+1

def g(x):
    return x**2

def h(x):
    return f(g(x))

x = np.array(range(-10, 10))
y = np.array([h(i) for i in x])
# lamba函数用法不明确
h2 = lamba x: f(g(x))
plt.plot(x, y, 'bo')