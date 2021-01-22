word = 'Hello'
letter1 = set(c for c in word)
letter2 = {c for c in word}

print(letter1)
print(letter2)
print(letter1 == letter2)
