small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)

small_primes.add(1)
print(small_primes)

small_primes.remove(1)
print(small_primes)
print(3 in small_primes)

print(4 in small_primes)
print(4 not in small_primes)
small_primes.add(3)
print(small_primes)

bigger_primes = set([5,7,11,13])
print(bigger_primes)
print(small_primes | bigger_primes)
print(small_primes & bigger_primes)
print(small_primes - bigger_primes)
print(bigger_primes - small_primes)

print('\nsmall_primes2 ')
small_primes2 = {2,3,5,5,3}
print(small_primes2)