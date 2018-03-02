# Author: Deddryk

"""
Solution to problem 43.

"""

from utils.misc import build_int, prev_perm

def substring_divisible(lst):
    if not build_int(lst[1:4]) % 2 == 0:
        return False
    if not build_int(lst[2:5]) % 3 == 0:
        return False
    if not build_int(lst[3:6]) % 5 == 0:
        return False
    if not build_int(lst[4:7]) % 7 == 0:
        return False
    if not build_int(lst[5:8]) % 11 == 0:
        return False
    if not build_int(lst[6:9]) % 13 == 0:
        return False
    if not build_int(lst[7:10]) % 17 == 0:
        return False
    return True

sum = 0
perm = range(9, -1, -1)
while perm[0] != 0:
    if substring_divisible(perm):
        sum += build_int(perm)
    perm = prev_perm(perm)
print sum
