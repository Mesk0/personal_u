"""Map用于将一个函数映射到一个输入列表的所有元素上"""
"""规范:map(function_apply, list_of_inputs)"""
"""map一般和lambda()一起使用"""

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x:x**2, items))
# map直接返回一个迭代器，所以需要用list进行转换
print(squared)

def multiply(x):
    return (x*x)

def add(x):
    return(x+x)

funcs = [multiply, add]     # 这个地方用到了闭包的知识
for i in range(5):
    value = map(lambda x:x(i), funcs)
    print(list(value))