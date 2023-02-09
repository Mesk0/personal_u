"""三元运算符允许⽤简单的⼀⾏快速判断,
⽽不是使⽤复杂的多⾏if语句,⽽且可以使代码简单可维护。
规范:condition_is_True if condition else condition_is_False"""

is_fat = True
state = "fat" if is_fat else "not fat"

fat = True
fitness = ("skinny", "fat")[fat]    # 1.三元运算符用元组表示的一种形式
print("Ali is ", fitness)   

condition = True
print(2 if condition else 1/0)  # 2.更通常使用三元运算符的方式
print(1/0, 2)[condition]    # 这行代码出现的错误说明了1形式的局限
# 不使⽤元组条件表达式的缘故是
# 因为在元组中会把两个条件都执⾏， ⽽ if-else的条件表达式不会这样
# 因为在元组中是先建数据， 然后⽤True(1)/False(0)来索引到数据。 
# ⽽if-else条件表达式遵循普通的if-else逻辑树