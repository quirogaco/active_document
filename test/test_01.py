"""
#1
def foo(n):
    for x in range(n):
        yield x**3

for x in foo(5):
    print(x),
"""

"""
print("foo" * 3)
print(2 ** 3)
"""

"""
#3
def foo(value):
    while (True):
        value = yield(value)


bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))
"""

"""
#4
example= "dhhdaanna"
print(example.replace("a", "b"))
"""

"""
#6
word = "positive"
print(word[:2])
"""

"""
def example(val):
    val = val + "4"
    val = val*2

    return val

print(example("jump"))
"""