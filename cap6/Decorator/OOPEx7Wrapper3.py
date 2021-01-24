from functools import wraps


def max_result(threshold):
    print('dentro de max_result')

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(func.__name__, ' Result is too big ({0}). Max allowed is {1}'.format(result, threshold))
            return 'Function ' + func.__name__ + ': ' + str(result)

        return wrapper

    return decorator


@max_result(75)
def cube(n):
    return n ** 3


@max_result(100)
def square(n):
    return n ** 2


@max_result(1000)
def multiply(a, b):
    return a * b


print(cube(5))
print(square(5))
print(multiply(5, 6))
