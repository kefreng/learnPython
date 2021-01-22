n = 39
remainders = []
while n > 0:
    remainder = n % 2
    remainders.insert(0, remainder)
    n //= 2

print(remainders)

print('----------')

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.insert(0, remainder)

print(remainders)

m = 83
print(bin(m)[2:])

print('----------')

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
position=0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1