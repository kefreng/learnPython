[]
list()
[1, 2, 3]
[x + 5 for x in [2, 3, 4]]

list((1, 3, 5, 7, 9))

list('hello')
"""
a = [1, 2, 1, 3]
a.append(13)
a

a.count(1)
a.extend([5,7])
a
a.index(13)

a.insert(0,17)
a

a.pop()
a.pop(3)
a

a.remove(17)
a

a.reverse()
a

a.sort()
a

a.clear()
a


a = list('hello')
a

a.append(100)
a

a.extend((1,2,3))
a

a.extend('...')
a

a = [1,3,5,7]
min(a)
max(a)
sum(a)
len(a)
b=[6,7,8]
a+b
a*2
"""
from operator import itemgetter
a = [(5,3),(1,3),(1,2),(2,-1),(4,9)]
sorted(a)
sorted(a,key=itemgetter(0))
sorted(a,key=itemgetter(0,1))
sorted(a,key=itemgetter(1))
sorted(a,key=itemgetter(1),reverse=True)