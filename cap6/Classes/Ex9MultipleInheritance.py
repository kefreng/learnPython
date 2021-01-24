class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}'.format(topleft, ratio))


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon):
    geometric_type = 'Regular Square'

    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
print(hexagon.plot(0.8, (75, 77)))

print('--------')

square = Square(12)
print(square.area())
print(square.get_geometric_type())
print(square.plot(0.93, (74, 75)))

print('--------')

print(square.__class__.__mro__)