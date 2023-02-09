"""lambda *args:func"""
add = lambda x,y:x+y
print(add(3, 5))

"1.lambda用于sort()排序"
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x:x[1])
print(a)
# sort()默认按照字母大小升序排序
# 输入reverse=True能降序排序
# 输入key=表达式，按照列表对表达式映射值大小，进行升序排列

"""2.lambda用于列表并行排序
data = zip(list1, list2)
data.sort()
list1,list2 = map(lambda t:list(t), zip(*data))"""

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs=['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'  # capitalize()作用返回一个首字母大写的字符串

edit_story(stairs, enliven)    # 上下两个代码等价
edit_story(stairs, lambda word:word.capitalize()+'!')
