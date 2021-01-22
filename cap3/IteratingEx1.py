people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Chile', 'Peru', 'Argentina', 'Brasil']

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

print('----------')

for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

print('----------')

for person, age in zip(people, ages):
    print(person, age)

print('----------')

for person, age, nat in zip(people, ages, nationalities):
    print(person, age, nat)

print('----------')

