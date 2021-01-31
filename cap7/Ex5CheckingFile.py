import os

filename = 'ejemplo.txt' 
path = os.path.dirname(os.path.abspath(filename))

print(os.path.isfile(filename))
print(path)