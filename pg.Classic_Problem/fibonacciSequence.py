from typing import Dict
memo:Dict[int, int] = {0: 0, 1: 1}  # our base cases

# 形参后的:为其注释，表示形参的类型
# ->为返回值的注释
def fib1(n: int) -> int:
    if n not in memo:   # base case
        memo[n] = fib1(n - 1) + fib1(n - 2)     # memoization
    return memo[n]

# unknowed Grammer
if __name__ == "__main__":
    print(fib1(1))
    print(fib1(5))
    print(fib1(10))
    print(fib1(50))
