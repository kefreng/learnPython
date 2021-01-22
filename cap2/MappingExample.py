a = dict(A=1, Z=-1)
b = {'A':1, 'Z':-1}
c = dict(zip(['A','Z'], [1,-1]))
d = dict([('A',1),('Z',-1)])
e = dict({'Z':-1,'A':1})

print(a == b == c == d == e)

print(list(zip(['h','e','l','l','o'], [1,2,3,4,5])))

print(list(zip(('hello'), range(1,6))))

d={}
d['a'] = 1
d['b'] = 2
print(len(d))
print(d['a'])
print(d)

del d['a']
print(d)

d['c']=3
print('c' in d)
print(3 in d)
print('e' in d)
d['c']=4
print(d)
#d.clear()
print(d)

print(d.keys())
print(d.values())
print(d.items())
d.clear()
print('\n-----------')
d = dict(zip('hello',range(5)))
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(3 in d.values())
print(('o',4) in d.items())
print(d)
d.popitem()
print(d)
d.pop('l')
print(d)
#d.pop('not-a-key')
print(d.pop('not-a-key','default-value'))
d.update({'another':'value'})
d.update(a=13)
print(d)
print(d.get('a'))
print(d.get('a',177))
print(d.get('b',100))
print(d.get('b'))

print('\nsetdefault: ')
d = {}
print(d.setdefault('a',1))
print(d)
print(d.setdefault('a',5))
print(d)

print('\nejemplo:')
d = {}
print(d.setdefault('a',{}).setdefault('b',[]).extend([1,2,3]))
print(d)