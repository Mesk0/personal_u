"""iterable、iterator、iteration"""

def generator_function():
    for i in range(10):
        yield i     # yield:生出。

for item in generator_function():
    print(item)