class Person:
    def __init__(self, age):
        self.age = age
        self.height = 100


class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 19 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18,99]')


class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        print('---seting value-----', age)
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18,99]')

person = PersonPythonic(39)
print(person.age)
person.age = 42
print(person.age)
#person.age = 100
print(person.__dict__.keys())

print('-----------')
p2 = PersonWithAccessors(39)
print(p2.get_age())
p2.set_age(89)
print(p2.get_age())

print('-----------')

p3 = Person(10)
print(p3.age)
print(p3.height)
p3.width = 56
print(p3.width)
