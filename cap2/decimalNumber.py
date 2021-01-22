from decimal import Decimal as D
print(D(3.14))
print(D('3.14'))
print(D('0.1') * D(3) - D('0.3'))
print(D('1.4').as_integer_ratio())