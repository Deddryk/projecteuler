# Author: Deddryk

"""
Solution to problem 37

"""

from bisect import bisect_left
from math import log10

from utils.primes import load_primes

def truncate_left(n):
    return n % 10**(int(log10(n)))

def truncate_right(n):
    return n / 10

primes = load_primes()
primes_set = set(primes)
num_truncatable_primes = 0
truncatable_primes_sum = 0
for prime in primes[bisect_left(primes, 10):]:
    if num_truncatable_primes == 11:
        break
    truncl, truncr = truncate_left(prime), truncate_right(prime)
    while truncl != 0 and truncr != 0:
        if truncl not in primes_set or truncr not in primes_set:
            break
        truncl = truncate_left(truncl)
        truncr = truncate_right(truncr)
    else:
        print prime
        num_truncatable_primes += 1
        truncatable_primes_sum += prime
print truncatable_primes_sum
