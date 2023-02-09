import numpy as np
import matplotlib.pyplot as plt

def f(u):
    return u**3 - 5*u**2 + 9

def exp(u):
    return np.e**u

x = np.linspace(-5, 5, num=100)
y = f(x)
plt.plot(x, y)
plt.plot(x, exp(x))
