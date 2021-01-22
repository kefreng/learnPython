def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2


def print_squares2(start, end):
    yield from (n ** 2 for n in range(start, end))


for n in print_squares(2, 5):
    print(n)

print('---------')
for n in print_squares2(2, 5):
    print(n)
