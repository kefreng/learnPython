age = 42
print(id(age))

age = 43
print(id(age))

class Person():
    def __init__(self, age):
        self.age = age

fab = Person(age=42)
print(fab.age)
print(id(fab))
print(id(fab.age))

fab.age = 25
print(id(fab))
print(id(fab.age))