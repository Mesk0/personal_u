"""Tuple"""
empty_tuple = ()    # （）创建空元组
print(empty_tuple)

one_marx = 'Groucho',   # 后缀逗号是创建元组的关键，不能缺少
print(one_marx)
ssc = 1,
print(ssc)

marx_tuple = 'Groucho', 'Chico', 'Harpo'    # 创建元组时可以不加圆括号
print(marx_tuple)    # 输出元组时会自动添加一对圆括号

a, b, c = marx_tuple    # 可以用元组同时赋值多个变量（元组解包）
print(a)
print(b)
print(c)

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password     # 元组对多个变量的值进行交换
print(password)
print(icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']   # 用列表数值创建元组
a = tuple(marx_list)
print(a)