"""zip()并行迭代"""

days=['monday', 'tuesday', 'wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day,":drink", drink, "-eat", fruit, '-enjoy', dessert)

# zip()在最短序列用完就会停止 
# zip()对匹配两个元组，返回值为一个整合在一起的可迭代的变量

english = 'monday', 'tuesday', 'wednesday'
french = 'lundi', 'mardi', 'mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))   # 运用dict和zip生成英法字典