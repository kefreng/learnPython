import shutil
import os

#carpeta inicial de ejemplo
BASE_PATH = 'D:\python\ejemplo'
os.mkdir(BASE_PATH)

#carpetas que estaran dentro del base path
path_b = os.path.join(BASE_PATH, 'A', 'B')
path_c = os.path.join(BASE_PATH, 'A', 'C')
path_d = os.path.join(BASE_PATH, 'A', 'D')

#crear las carpetas A/B , A/C
os.makedirs(path_b)
os.makedirs(path_c)

#crear archivos dentro de la carpeta A/B
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(os.path.join(path_b, filename), 'w') as stream:
        stream.write(f'Some content here in {filename}\n')

#mover contenido de la carpeta B a la carpeta D similar a comando mv
shutil.move(path_b, path_d)

#en la carpeta A/D , mover archivo ex1 a ex1d
shutil.move(
    os.path.join(path_d, 'ex1.txt'),
    os.path.join(path_d, 'ex1d.txt')
)

print(os.path.isfile(path_c))

