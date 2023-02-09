"""filter用于过滤列表中的元素"""

number_list = range(-5, 5)
less_than_zero = filter(lambda x:x < 0, number_list)
print(list(less_than_zero))   # filter返回一个迭代器，所以需要加list转换