def document_it(func):
    # *args为位置参数，传递一个可变实参数列表给函数实参，作为元组tuple使用
    # **kwargs为关键词参数，传递一个可变关键词参数的字典给函数实参
    # args只能位于kwargs的前面
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function()


def add_ints(a, b):
    return a + b


cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

