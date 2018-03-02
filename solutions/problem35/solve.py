# Author: Deddryk

"""
Solution to problem 35

"""

from math import log10
from bisect import bisect_left

from utils.primes import load_primes

def num_digits(n):
    return int(log10(n)) + 1

def rotate(n):
    return n % 10 * 10**int(log10(n)) + n / 10

primes = load_primes()
primes = primes[bisect_left(primes, 100):bisect_left(primes, 1000000)]
prime_set = set(primes)
count = 13
while len(prime_set) > 0:
    n = prime_set.pop()
    for i in xrange(num_digits(n) - 1):
        n = rotate(n)
        if n not in prime_set:
            break
        prime_set.remove(n)
    else:
        count += num_digits(n)
print count

