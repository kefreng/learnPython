class A:
    label = 'a'


class B(A):
    #label = 'b'
    pass


class C(A):
    label = 'c'


class D(B, C):
    pass


d = D()
print(d.label)
print(d.__class__.mro())