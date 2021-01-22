from math import sqrt

mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]
print(triples)
'''
triples = filter(lambda triple: triple[2].is_integer(), triples) 
triples = list(map(lambda triple: triple[:2] + (int(triple[2]),), triples))
print(triples)

x = (2,3) + (4,)
print(x)
'''
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples)
