greet_old = 'Hello %s '
greet_old % 'Felix'

greet_positional = 'Hello {} {}!'
greet_positional.format('Felix', 'Flores')

greet_positional_idx = 'This is {0}! {1} loves {0}'
greet_positional_idx.format('Python', 'Felix')

keyword = 'Hello, my name is {name}, {last_name}'
keyword.format(name='Felix', last_name='Flores')

name='Felix'
age = 32
f"Hello! My name is {name} and I'm {age}"
from math import pi
f"No arguing with {pi}, it's irrational...."