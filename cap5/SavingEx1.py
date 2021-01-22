print(range(7))

print(list(range(7)))

_ = list
print(_(range(7)))

print(_(map(lambda *a: a, range(3), 'abc' )))
print(_(map(lambda *a: a, range(3), 'abc' , range(4,7))))

print(_(map(lambda *a: a, (), 'abc' )))

print(_(map(lambda *a: a, (1,2), 'abc' )))

print('--------')
print(_(map(lambda *a: a, (1,2,3,4), 'abc')))
