# Author: Deddryk

"""
Solution to problem 25.

"""

from math import log10

f1 = 1
f2 = 1
cur = 2
while log10(f2) + 1 < 1000:
    cur += 1
    f1, f2 = f2, f1 + f2
print cur
