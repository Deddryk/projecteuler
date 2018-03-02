# Author: Deddryk
"""
Solution to problem 12.

"""

from utils.primes import factor
from utils.misc import product

def num_factors(n):
    """
    Calculate the number of factors n has

    """
    prime_factors = factor(n)
    return product([x + 1 for x in factor(n).values()])

triangle_num = 3
step_size = 3
while num_factors(triangle_num) <= 500:
    triangle_num += step_size
    step_size += 1
print triangle_num

