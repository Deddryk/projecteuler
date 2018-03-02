# Author: Deddryk

"""
Solution to problem 16.

Easy in python. Just calculate 2^1000 and sum the digits.

"""

print sum([int(x) for x in str(2 ** 1000)])
