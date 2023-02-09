def factorial1(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def power1(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n-1)

print(factorial1(50))
print(factorial2(50))
print(power(2, 116))
print(power1(2, 116))