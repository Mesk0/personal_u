def colltaz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

def run():
    i = int(input("please input a number: "))
    while i != 1:
        print(colltaz(i))
        i = colltaz(i)


# input()输入的数字，记得用int()转换为数字类型，否则会默认输入类型为字符串
try:
    run()
# except子句应具体，比如ValueError
except ValueError:
    print("please input a int number")
    # 此程序可以采用递归，后续学习改进
    run()