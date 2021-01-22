cubes = [k ** 3 for k in range(10)]
print(cubes)
print(cubes)
print(type(cubes))

cubes_gen = (k ** 3 for k in range(10))
print(cubes_gen)
print(type(cubes_gen))
_ = list
print(_(cubes_gen))
print(_(cubes_gen))

print('------------')


def adder(*n):
    # print(n, '-', sum(n))
    return sum(n)


s1 = sum(map(lambda *n: adder(*n), range(100), range(1, 101)))
print(s1)
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s2)

print('------------')
cubes = [x ** 3 for x in range(10)]
print(cubes)

odd_cubes1 = filter(lambda cube: cube % 2, cubes)
print(_(odd_cubes1))
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(_(odd_cubes2))
print('------------')

N = 20
cubes1 = map(lambda n: (n, n ** 3),
             filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N)))

print(_(cubes1))

cubes2 = ((n, n ** 3) for n in range(N) if n % 3 == 0 or n % 5 == 0)
print(_(cubes2))
print('-----------')

s1 = sum([n**2 for n in range(2**6)])
s2 = sum((n**2 for n in range(2**6)))
s3 = sum(n**2 for n in range(2**6))
print(s1, s2, s3)

print('-----------')
lista_test = list(map(lambda n: n, zip('ABC', (1, 2, 3, 4))))
lista_test2 = [(n, m) for n in 'ABC' for m in (1, 2, 3, 4)]
print(lista_test)
print(lista_test2)
