def get_square(n):
    return [x**2 for x in range(n)]

print(get_square(10))

def get_square_gen(n):
    for x in range(n):
        yield x**2

print(list(get_square_gen(10)))

squares = get_square_gen(4)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
#print(next(squares))
print('----------')

def geometric_progression(a,q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k+=1

for n in geometric_progression(2,5):
    print(n)