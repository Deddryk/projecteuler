"""
Solution to project euler problem 7

I solved this using the primes module built for problem 3.  Admittedly,
I had to play around with the max prime limit.

"""

from ..utils.primes import load_primes

print load_primes()[10000]
