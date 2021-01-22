def minimum(*n):
    print(type(n))
    print(n)
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)
print('----------')
minimum()
print('----------')

def func(*args):
    print(args)

values = (1,3,-7,9)
func(values)
func(*values)

