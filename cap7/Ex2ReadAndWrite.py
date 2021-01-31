with open('print_example.txt', 'w') as fw:
    print('Hey I am printin into a file!!!', file=fw)
    print('Hey I am printin into a file!!!', file=fw)


with open('ejemplo.txt') as f:
    for line in f:
        print(line.rstrip())
    lines = [line.rstrip() for line in f]

print('\n'.join(lines))

with open('ejemplo_copy.txt', 'w') as fw:
    fw.write('\n'.join(lines))