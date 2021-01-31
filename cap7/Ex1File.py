fh = open('ejemplo.txt')

try:
    for line in fh:
        print(line.strip())
finally:
    fh.close()


print('---- content manager -----')
with open('ejemplo.txt') as fh:
    for line in fh:
        print(line.strip())

