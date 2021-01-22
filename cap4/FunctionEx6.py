def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)

print('----------')


def func2(a, b, c):
    print(a, b, c)

func(a=1, b=2, c=3)

print('----------')

def func3(a, b=4, c=88):
    print(a,b,c)

func3(1)
func3(b=5, a=7, c=9)
func3(42, c=9)
func3(42,43,44)
#func3(b=1, c=2, 42)