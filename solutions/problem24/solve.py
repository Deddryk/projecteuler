# Author: Deddryk

"""
Solution to problem 24

To do this quickly, I use the fact that between 0123456789
and 1023456789 there are 10! permutations.  This loops through
each digit and finds the highest it can be without going over
1000000 allowing it to run very quickly.

"""

from math import factorial

digit = 10
available = range(10)
permutation = []
cur_perm = 1
while digit > 0:
    n = 0
    while cur_perm + factorial(digit - 1) <= 1000000:
        cur_perm += factorial(digit - 1)
        n += 1
    permutation.append(available.pop(n))
    digit -= 1
print "".join(map(str, permutation))


    
    
