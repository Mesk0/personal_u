def fib5(n: int) -> int:
    if n == 0:
        return n    # special case
    last: int = 0
    next0: int = 1
    # Tuple解包
    """要领就是last被设置为next的上一个值，
    next被设置为last的上一个值加上next的上一个值。
    这样在last已更新而next未更新时，就不用创建临时变量以存储next的上一个值了。"""
    for _ in range(1, n):
        last, next0 = next0, last + next0
    return next0

print(fib5(50))