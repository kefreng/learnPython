_ = list
squares = []
for n in range(10):
    squares.append(n ** 2)

print(squares)

squares = (map(lambda x: x ** 2, range(10)))
print(_(squares))

print([n ** 2 for n in range(10)])

# odd numbers
odd1 = list(map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10))))
print(odd1)

odd2 = list(n ** 2 for n in range(10) if not n % 2)
print(odd2)

print(odd1, odd1 == odd2)