import numpy as np
from scipy.optimize import curve_fit

def Pfun(t, a, b, c):
    return a*np.exp(b*t[0])+c*t[1]**2

x0 = np.array([6, 2, 6, 7, 4, 2, 5, 9])
y0 = np.array([4, 9, 5, 3, 8, 5, 8, 2])
z0 = np.array([5, 2, 1, 9, 7, 4, 3, 3])
xy0 = np.vstack((x0, y0))
popt,pcov = curve_fit(Pfun, xy0, z0)
# popt,pcov = curve_fit(func, xdata, ydata)
# func是拟合的函数，xdata是自变量的观测值，ydata是函数的观测值
# popt是拟合的参数，pcov是参数的协方差矩阵
print("a, b, c的拟合值为:", popt)