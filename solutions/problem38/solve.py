# Author: Deddryk

"""
Solution to problem 38

"""

from utils.misc import used_digits, num_digits

def is_pandigital(n):
    return len(used_digits(n)) == num_digits(n)
    
concatenated_pandigitals = set()
for i in xrange(10, 10000):
    multiplier = 1
    concatenated_product = 0
    while num_digits(concatenated_product) < 9:
        next_part = i * multiplier
        multiplier += 1
        concatenated_product = concatenated_product * 10**num_digits(next_part) + next_part
        if not is_pandigital(concatenated_product): break
        if 0 in used_digits(concatenated_product): break
    else:
        if num_digits(concatenated_product) == 9:
            concatenated_pandigitals.add(concatenated_product)
print max(concatenated_pandigitals)
