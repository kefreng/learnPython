x = 0
y = 0
def f():
    x = 1
    y = 1
    class C:
        print(x, y)  # What does this print?
        x = 5
f()