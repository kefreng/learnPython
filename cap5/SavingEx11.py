def get_squares_gen(n):
    for n in range(n):
        yield n ** 2


squares = get_squares_gen(3)
print(squares.__next__())
print(squares.__next__())
print(squares.__next__())
# print(squares.__next__())
print('--------')


def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1


c = counter()
print(next(c))
print(c.send('Wow!'))
print(next(c))
print(c.send('Q'))
# print(next(c))
