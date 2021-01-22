from functools import reduce
from operator import mul, add


def factorial(n):
    return reduce(mul, range(1, n + 1), 1)


def sum(n):
    return reduce(add, range(1, n + 1))


f5 = factorial(5)
print(f5)
print(sum(5))


def moddiv(a, b):
    return a // b, a % b


print(moddiv(20, 7))
