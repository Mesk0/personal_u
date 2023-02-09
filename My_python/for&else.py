""" for/else基本结构
for item in container:
    if search_something(item):
        process(item)
        break
else
    not_found_in_container()"""

"求2~10的因子和质数"
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, 'x', n/x)
            break
    else:
        print(n, 'is a prime number')

# 循环停止的两种情况：1.break出发；2.循环次数用完，自动结束。
# for循环的else从句在循环正常结束（2条件）之后执行，意味着循环中没有遇到break