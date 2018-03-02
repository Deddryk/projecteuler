# Author: Deddryk

"""
Solution to problem 29

This is very quick and easy with python's set capabilities.  Just
calculate every power and add it to the set

"""

powers = set()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        powers.add(a**b)
print len(powers)
