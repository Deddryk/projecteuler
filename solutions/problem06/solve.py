#Author: Deddryk
"""
Solution to project euler problem 6

Easy one in python since big numbers are built in.
Just sum the squares, square the sum, and subtract.

"""

from math import pow

sum_of_squares = sum([i * i for i in xrange(101)])
square_of_sums = int(pow(sum(xrange(101)), 2))

print square_of_sums - sum_of_squares
