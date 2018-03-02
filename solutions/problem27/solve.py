# Author: Deddryk

"""
Solution to problem 27

Essentially this solution loops through every possible coefficient
a and b and checks to see how many primes are generated for consecutive
n starting at 0.  Some time is saved by using only primes for b since
for the case n = 0, b must be prime.  It uses the utils.primes module
for prime generation and slices the generated list to all primes < 1000,
then makes a set for fast in checks.

"""

from utils.primes import load_primes

primes = set(load_primes())
small_primes = [x for x in primes if x < 1000]

def count_primes(a, b):
    count = 1
    n = 1
    while n*n + a*n + b in primes:
        count += 1
        n += 1
    return count

most = (40, 1, 41)
for a in xrange(-999, 1000):
    for b in small_primes:
        primes_gen = count_primes(a, b)
        if primes_gen > most[0]:
            most = (primes_gen, a, b)
print most[1] * most[2]
