# Author: Deddryk

"""
Solution to problem 39

This solution relies on euclids algorithm for generating pythagorean triples:
    Given coprime positive integers m, n < m, with m - n odd, a pythagorean
    triple is formed with a = m*m - n*n, b = 2*m*n, c = m*m + n*n
All primitive pythagorean triples are formed with this generator, so multiplying
each one by k in (1, x) while a+b+c < 1000 forms all pythagorean triples where
p is less than 1000.

I generate every pythagorean triple, and store the number of times each perimeter
is generated.

Runs in ~ .1 seconds

"""

from utils.misc import gcd

perimeters = dict([(x, 0) for x in xrange(12, 1001)])
for m in xrange(2, 21):
    p = 12
    n = m%2 + 1
    while n < m and p <= 1000:
        if gcd(m, n) > 1:
            n += 2
            continue
        p = 2*m*m + 2*m*n
        k = 1
        while k*p <= 1000:
            perimeters[k*p] += 1
            k += 1
        n += 2
print max(perimeters, key=lambda k: perimeters[k])
