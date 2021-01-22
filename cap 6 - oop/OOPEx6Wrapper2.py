from time import sleep, time
from functools import wraps


def measure(func):
    print('wrapper measure')
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('dentro de wrapper measure')
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took: ', time() - t)
        return result
    return wrapper


def max_result(func):
    print('wrapper max_result')
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('dentro de wrapper max_result')
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'.format(result))
        else:
            print('result ok')
        return result
    return wrapper


@measure
@max_result
def cube(n):
    return n ** 3

print('------')
print(cube(2))
print('------')
print(cube(5))
