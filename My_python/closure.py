"""closure(闭包):是一个可以由另一个函数动态生成的函数"""

def knight2(saying):
    def inner2():
        return "We are the knights who say:'%s'"%saying
    return inner2
# return inner2并没有调用inner2()函数，而是变成了一个叫inner2()的闭包
# 相当于knight只是一个改变inner2()函数(闭包)内部参数的函数，而且没用调用闭包inner2
# 这是闭包与内部函数的区别

a = knight2('Duck')     # 这一步并没有调用inner2闭包，而是动态生成了inner2新的参数值
b = knight2('Hasenpfeffer')
print(type(a))  # 注意a,b的类型都是函数，也是闭包
print(type(b))  
print(a) 
print(b)
print(a())
print(b())