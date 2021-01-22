def func(a, b, c=7, *args, **kwargs):
    print('a,b,c:', a, b, c)
    print('args:', args)
    print('kwargs', kwargs)
    print('--------')


func(1, 2, 3, *(5, 6, 7), **{'A': 'a', ' B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b')


def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a,b:', a, b)
    print('c,d:', c, d)
    print('args:', args)
    print('kwargs', kwargs)
    print('--------')


func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')


def additional(*args, **kwargs):
    print(args)
    print(kwargs)
    print('--------')


args1 = (1, 2, 3)
args2 = [4, 5]
kwargs1 = dict(option1=10, option2=20)
kwargs2 = {'option3': 30}
additional(*args1, *args2, **kwargs1, **kwargs2)


def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)
    print('--------')

func()
#func()
func(a=[1,2,3], b={'B':1})
func()