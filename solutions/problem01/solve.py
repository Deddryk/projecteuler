# Author: Deddryk
"""
Solution to project euler problem 1.

This is a one liner because I solved this with pencil and paper and used
python as a calculator.

The sum of all multiples of 3 under 1000 is 3 + 6 + ... + 999.
This is equal to 3 * (1 + 2 + ... + 333).
Hopefully everyone remembers that 1 + 2 + ... + 333 is equal to
(1 + 333) * 333 / 2
Similarly for multiples of 5 we get 5 * (1+199) * 199 / 2

This leaves us with extra however, because numbers that are multiples
of both 5 and 3 were included twice.  To solve this we subtract the
multipes of 15 (LCM of 5 and 3)

"""

print 3 * 334 * 333 / 2 + 5 * 200 * 199 / 2 - 15 * 67 * 66 / 2
