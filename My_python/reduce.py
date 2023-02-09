"""reduce用于对一个列表进行一个计算并返回结果"""

from functools import reduce
product = reduce((lambda x,y: x*y), [1, 2, 3, 4])
print(product)