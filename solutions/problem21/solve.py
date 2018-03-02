# Author: Deddryk

"""
Solution to problem 21.

"""

from utils.primes import sum_of_divisors

total = 0
for i in xrange(2, 10000):
    sod = sum_of_divisors(i)
    if sod > i and sum_of_divisors(sod) == i:
        total += i + sod
print total

    
