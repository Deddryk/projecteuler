# Author: Deddryk

"""
Solution to problem 34.

"""

from math import factorial

def sodf(x):
    sum = 0
    while x > 0:
        sum += factorial(x % 10)
        x /= 10
    return sum

sum = 0
for i in xrange(10, 1854721):
    if i == sodf(i):
        print(i)
        sum += i
print(sum)
