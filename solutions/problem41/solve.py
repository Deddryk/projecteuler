# Author: Deddryk

"""
Solution to problem 41.

This is solved by checking every permutation of the digits 1..n
for n in 9..2 for primality.

"""

from utils.primes import probable_prime
from utils.misc import prev_perm, build_int

x = range(9, 0, -1)

for num_digits in range(9, 1, -1):
    x = range(num_digits, 0, -1)
    while x != range(1, num_digits + 1):
        if probable_prime(build_int(x)):
            print(build_int(x))
            exit()
        x = prev_perm(x)
