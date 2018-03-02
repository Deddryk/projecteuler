# Author: Deddryk
"""
Soution to problem 9.

This is another straightforward solution.  I iterate over all possible
combinations of a, b, and c and stop when I find the combination where
a^2 + b^2 = c^2.

To save some time, I used the fact that a < b < c to limit the possible
combinations.  a must be less than 333 because b must
be greater than a and c must be greater than b.  333 + 334 + 335 = 1002.
b must be less than (1000-a) / 2 + 1 so that c can be greater than b and
sum to 1000.

"""

for a in xrange(1, 333):
    for b in xrange(a + 1, (1000-a) / 2 + 1):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print a * b * c
            exit()
