"""inner function(内部函数)：在函数内部定义另一个函数"""
# 调用外部函数时同时也调用了内部函数

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(type(outer(4, 7)))
print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say:'%s'"%quote
    return inner(saying)

print(type(knights('Ni')))