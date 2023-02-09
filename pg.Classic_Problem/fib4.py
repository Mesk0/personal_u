from functools import lru_cache

# functool模块的lru_cache装饰器，maxsize为最多缓存次数
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:   # base case
        return n
    return fib4(n - 2) + fib4(n - 1)    # recursive case

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))

