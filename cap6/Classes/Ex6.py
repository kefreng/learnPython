class Rectangule:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b


r = Rectangule(10, 4)
print(r.side_a, r.side_b)
print(r.area())
print(Rectangule.area(r))

r2 = Rectangule(7, 3)
print(r2.area())
