# Author: Deddryk

"""
Solution to problem 20

"""

from math import factorial, log10, floor

n = factorial(100)
s = 0
while n != 0:
    s += n % 10
    n /= 10
print s
