# Author: Deddryk
"""
Miscelaneous utilities

"""

from operator import mul
from math import log10

def product(numbers):
    """
    Return the product of a list of numbers

    """
    return reduce(mul, numbers)

def used_digits(n):
    """
    Return a set containing every digit used in n

    """
    digits = set()
    while n > 0:
        digits.add(n%10)
        n /= 10
    return digits

def gcd(a, b):
    """
    Return the greatest common divisor of a and b

    """
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
    
def num_digits(n):
    """
    Return the number of digits used by n when reprented
    in decimal notation

    """
    if n == 0: return 1
    return int(log10(n)) + 1

def is_pandigital(n):
    """
    Return whether a number is pandigital
    
    """
    return len(used_digits(n)) == num_digits(n)

def prev_perm(perm):
    """
    Given a permutation perm, return the previous permutation
    in lexicographic order.

    Elements of perm must be unique and support the < operator
    
    """
    cur_perm = [x for x in perm]
    temp = [cur_perm.pop()]
    while cur_perm[-1] < temp[-1]:
        temp.append(cur_perm.pop())
    max = -1
    while(-max < len(temp) and temp[max - 1] < cur_perm[-1]):
        max -= 1
    t = temp[max]
    temp[max] = cur_perm[-1]
    cur_perm[-1] = t
    cur_perm.extend(temp)
    return cur_perm

def build_int(lst):
    """
    Given lst, a list of integers i where 0 <= i < 10 contruct the
    int in base 10 represented by lst[0]lst[1]...lst[n]
    
    """
    my_lst = [x for x in lst]
    number = 0
    i = len(my_lst) - 1
    while len(my_lst) > 0:
        number += my_lst.pop(0) * 10**i
        i -= 1
    return number
