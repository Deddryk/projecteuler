# Author: Deddryk

"""
Solution to problem 32.

This solution is ugly but it works quickly.  Using sets I limit the search space
to only those numbers that do not have similar digits, and only 3 or 4 digits.

"""

from math import log10, floor
from utils.misc import used_digits

digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
m1 = set()
m2 = set()
products = set()
for i in digits:
    for j in digits - used_digits(i):
        for k in digits - used_digits(i) - used_digits(j):
            m1.add(100*i + 10*j + k)
            for l in digits - used_digits(i) - used_digits(j) - used_digits(k):
                m2.add(1000*i + 100*j + 10*k + l)
for i in m1:
    m3 = set()
    for j in digits - used_digits(i):
        for k in digits - used_digits(i) - used_digits(j):
            m3.add(10 * j + k)
    for j in m3:
        if floor(log10(i*j)) == 3 and len(digits - used_digits(i) - used_digits(j) - used_digits(i*j)) == 0:
            products.add(i*j)

for i in m2:
    for j in digits - used_digits(i):
        if floor(log10(i*j)) == 3 and len(digits - used_digits(i) - used_digits(j) - used_digits(i*j)) == 0:
            products.add(i*j)
print sum(products)
