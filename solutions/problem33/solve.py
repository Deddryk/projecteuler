# Author: Deddryk

"""
Solution to probelm 33

This solution checks every possible value of a and b for a/b

"""

from utils.misc import used_digits, gcd
from utils.primes import factor

num = 1
den = 1

def check_eq(a, b, c, d, num, den):
    if a % 10 == 0 and b % 10 == 0: return num, den
    if a / gcd(a, b) == c / gcd(c, d) and b / gcd(a, b) == d / gcd(c, d):
        num *= a
        den *= b
    return num, den

for i in xrange(10, 100):
    for j in xrange(i + 1, 100):
        if len(used_digits(i) & used_digits(j)) > 0:
            if i / 10 == j / 10:
                num, den = check_eq(i, j, i%10, j%10, num, den)
            elif i / 10 == j%10:
                num, den = check_eq(i, j, i%10, j/10, num, den)
            elif i % 10 == j / 10:
                num, den = check_eq(i, j, i/10, j%10, num, den)
            else:
                num, den = check_eq(i, j, i/10, j/10, num, den)
print den / gcd(num, den)
