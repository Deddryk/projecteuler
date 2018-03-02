# Author: Deddryk

"""
Solution to problem 40

"""

from utils.misc import product

i = 1
fractional_part = "1"
while len(fractional_part) < 1000000:
    i += 1
    fractional_part += str(i)
values = [int(fractional_part[10**x - 1]) for x in xrange(6)]
print product(values)
