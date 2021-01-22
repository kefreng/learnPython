_ = list
test = [2, 5, 8, 0, 0, 1, 0]
print(_(filter(None, test)))
print(_(filter(lambda x: x, test)))
print(_(filter(lambda x: x > 4, test)))

