from cap6.Classes.Ex7InheritanceComposition import Car, RaceCar, F1Car

car = Car()
racecar = RaceCar()
f1car = F1Car()
cars = [(car,'car'),(racecar,'racecar'),(f1car,'ficar')]
car_classes = [Car,RaceCar,F1Car]


for car, car_names in cars:
    for class_ in car_classes:
        belongs = isinstance(car,class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_names, msg, class_.__name__)

print('-----')

for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format(
            'is' if is_subclass else 'is not'
        )
        print(class1.__name__,msg, class2.__name__)