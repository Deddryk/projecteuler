# Author: Deddryk
 
"""
Solution to problem 23.

This solution first generates a set of all abundant numbers.
It then loops through all numbers less than 28124, subtracting every abundant
number until it finds a result that is in the abundant set.  If it does not
find a result, it is added to the running sum.  Runs in 2.5 seconds on
my system.  Could probably be improved

"""

from utils.primes import sum_of_divisors

abundants = set([x for x in xrange(1, 28124) if sum_of_divisors(x) > x])
non_abundant_sum = 0
for i in reversed(xrange(1, 28124)):
    for num in abundants:
        if i - num in abundants:
            break
    else:
        non_abundant_sum += i
print non_abundant_sum
