# 常规列表创建方式
number_list0 = []
for number in range(1, 6):
    number_list0.append(number)
print(number_list0)

number_list1 = list(range(1, 6))
print(number_list1)


'''List conprehensions'''
# 列表推导式
# 第一个number为表达式，作为变量储存值;第二个number为循环变量。
number_list2 = [number for number in range(1, 6)]
print(number_list2)

number_list3 = [number-1 for number in range(1, 6)]
print(number_list3)

# 加上条件表达式的列表推导式
# 第三个number条件是对于第二个number而言，即条件表达式对于循环变量起作用。
a_list0 = [number for number in range(1, 6) if number % 2 == 1]
print(a_list0)

a_list1 = [number-1 for number in range(1, 6) if number % 2 == 1]
print(a_list1)

# 嵌套循环创建元组
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print((row, col))

# 嵌套循环元组列表推导式
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)


'''Dict conprehensions'''
# 典型格式
# [key_expression:value_expression for expression in iterable]
# letter为key,word.count(letter)为value。

word = 'letters'
letter_counts1 = {letter:word.count(letter) for letter in word}
print(letter_counts1)

letter_counts2 = {letter:word.count(letter) for letter in set(word)}
print(letter_counts2)


"""Tuple conprehensions"""
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)


'''generotor conprehensions'''
number_thing = (number for number in range(1, 6))
print(number_thing)