# Author: Deddryk

"""
Solution to problem 28.

This solution uses a running total, calculating only the diagonal numbers of the
spiral by increasting the step size by two every forth step.

"""

total, cur = 1, 1
for i in xrange(1, 1001, 2):
    for j in xrange(4):
        cur += i + 1
        total += cur
print total
