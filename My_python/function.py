# 1.None与False的区别
"""None作为布尔值与False等价，但是有其他区别"""
thing = None
if thing:
    print("It's spme thing")
else:
    print("It's no thing")

# 2.默认参数值，不能将可变的数据类型作为默认参数值
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def works(arg):
    result = []
    result.append(arg)

# 3.*将一组可变数量的位置参数集合成参数值的元组（可变位置参数）
def print_args(*args):
    print('Positional argument tuple:', args)

print_args(3, 2, 1, 'wait!', 'uh...')

# 4.**将一组可变数量的关键词参数集合成键值对的字典（可变关键词参数）
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# 5.