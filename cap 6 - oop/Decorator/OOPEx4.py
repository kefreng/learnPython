from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)

    return wrapper


f = measure(f)
f(0.2)
f(sleep_time=0.3)
print(f.__name__)

print('---')


def func_suma(a=1, b=0):
    return a + b


def sum_values(func):
    def wrapper(*args):
        value = func(*args)
        return value

    return wrapper


sum = sum_values(func_suma)
print(sum(2, 3))
