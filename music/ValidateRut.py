from itertools import cycle

def digito_verificador(rut):
    r = ''.join(r for r in str(rut) if r.isalnum())
    reversed_digits = map(int, reversed(str(r)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

print(digito_verificador('16.866.929'))