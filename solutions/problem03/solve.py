# Author: Deddryk
"""
Solution to project euler problem 3

If you use a unix or linux system odds are it has the factor command and
you can solve this problem with that.  However, for educational purposes
and just for fun, I implemented my own version of factor as well as a
prime number generator.  Since these functions will be useful later on
I put them into a module within the utils package

"""

from utils import primes

print max(primes.factor(600851475143).iterkeys())

