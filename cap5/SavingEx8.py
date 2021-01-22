from string import ascii_lowercase

lettermap = dict((c, k)
                 for k, c in enumerate(ascii_lowercase, 1))

lettermap2 = {c: k
              for k, c in enumerate(ascii_lowercase, 1)}

lm = map(lambda x: {x[1], x[0]}, enumerate(ascii_lowercase, 1))

print(lettermap)
print(list(lm))
print(lettermap2)

word = 'Hello'
position = {c: k for k, c in enumerate(word)}
print(position)
