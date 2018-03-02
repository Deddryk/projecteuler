# Author: Deddryk

"""
Solution to probelm 30.

"""

def sum_of_digits5(n):
    result = 0
    while n > 0:
        result += (n % 10)**5
        n /= 10
    return result

total = 0
for i in xrange(2, 400000):
    if sum_of_digits5(i) == i:
        total += i
print total

