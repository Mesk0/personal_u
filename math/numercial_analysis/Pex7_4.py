import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

"""一维插值"""
# 基本调用格式：interp1d(x, y, kind = 'linear')
# ‘zero':0阶， ’slinear':1阶, 'quadratic':2阶
# ‘cubic':3阶。

x = np.arange(0, 25, 2)
y = np.array([12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13])
xnew = np.linspace(0, 24, 500)
f1 = interp1d(x, y); y1 = f1(xnew)
f2 = interp1d(x, y, 'cubic'); y2 = f2(xnew)
plt.rc('font', size=16); plt.rc('font', family='SimHei')
plt.subplot(121); plt.plot(xnew, y1); plt.xlabel("(A)分段线性插值")
plt.subplot(122); plt.plot(xnew, y2); plt.xlabel("(B)三次样条插值")
plt.savefig(r"e:/BaiduSyncdisk/python/numercial_analysis/figure7_4.png", dpi=500)
plt.show()