_ = list
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print(_(zip(avgs, grades)))

print(_(map(lambda *a: a, avgs, grades)))

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
print(_(zip(a,b,c)))
maxs = map(lambda n: max(*n), zip(a,b,c))
print(_(maxs))
print('---------')
maxs2 = map(lambda *n: max(n), a,b,c)
print(_(maxs2))

print('---------')
z = [(5, 3, 6), (9, 7, 8), (2, 1, 0), (4, 9, 5), (7, 2, 3)]
print(*z)

