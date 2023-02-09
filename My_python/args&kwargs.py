"""*args"""
# 用来发送一个非键值对的可变数量的参数列表的函数，*是必须的，args可以任意命名。
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

"""*kwargs"""
# 用于发送不定长度的键值对，作为参数传递给函数。
def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob", age="23")