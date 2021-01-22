from random import randint


def func(**kargs):
    kargs['nuevo'] = randint(0,100)
    print(kargs)


func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))

print('-------')
