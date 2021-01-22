surnames = ['Rivest','Shamir','Adleman']
for position in range(len(surnames)):
    #print(position, surnames[position])
    print( surnames[position][0], end='')
print('----------')

for surname in surnames:
    print(surname)
print('----------')

for position, surname in enumerate(surnames):
    print(position, surname)