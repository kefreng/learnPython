def fibionacci(N):
    # print(N)
    if N == 0 or N == 1:
        return 1
    if N > 0:
        return fibionacci(N - 1) + fibionacci(N - 2)


print(fibionacci(10))

print('--------')


def fibionacci2(N):
    """Return all fibionacci numbers up t N."""
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        # print(result[:])
        # print(result[-2:])
        next_n = sum(result[-2:])
    return result


# print(fibionacci2(0))
# print(fibionacci2(1))
print(fibionacci2(10))

print('---------')


def fibionacci3(N):
    """Return all fibionacci number up to N."""
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b


print(list(fibionacci3(0)))
print(list(fibionacci3(1)))
print(list(fibionacci3(10)))

print('---------')


def fibionacci4(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

print(list(fibionacci4(0)))
print(list(fibionacci4(1)))
print(list(fibionacci4(10)))

print('---------')
arr = []
def fibionacci5(N):
    # print(N)
    if N <= 1: 
        return N
    else:
        return (fibionacci5(N - 1) + fibionacci5(N - 2))




print(fibionacci5(3))
print(arr)