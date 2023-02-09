import numpy as np

a = np.array([2, 4, 8, 20, 16, 30])
b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (10, 9, 1, 2, 3), (4, 5, 6, 8, 9.0)))
print("一维数组:", a)
print("二维数组:\n", b)

a1 = np.arange(4, dtype=float)
b1 = np.arange(0, 10, 2, dtype=int)
c1 = np.empty((2, 3), int)
d1 = np.linspace(-1, 2, 5)
e1 = np.random.randint(0, 3, (2, 3))
