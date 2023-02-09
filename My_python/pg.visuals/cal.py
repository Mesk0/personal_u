def average(*numbers):
    s = 0
    a = 0
    for number in numbers:
        a = a + int(number)
        s += 1
    b = a/s
    return b


