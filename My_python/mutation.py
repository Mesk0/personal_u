"""mutabel&immutable"""

foo = ['hi']
print(foo)

bar = foo
bar += ['bye']
print(foo)

# （mutablilty）对于可变数据类型，将一个变量赋值给另一个可变类型的变量，
# 对这个数据的任意改动会同时反映到两个变量上去，新变量只是老变量的别名。

def add_to(num, target = []):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))

# python中函数被定义，默认参数只会运算一次，不是每次调用都会重新计算
# 默认参数不要设置为可变类型

def add_to1(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to1(42))
print(add_to1(43))
print(add_to1(44))