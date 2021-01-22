def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100


def my_function():
    test = 1
    print('my_function:', test)


test = 0
my_function()
print('global: ', test)

