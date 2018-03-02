#Author: Deddryk
"""
Solution to Project Euler problem 4

I built a function to reverse an integer in order to check if it was a
palindrome.  Then I count backwards from 999 on two integers, 
multiplying them together and checking if the product is a palindrome
and save the maximum palindrome.

I save time by counting backwards and breaking the inner loop when the
current product is less than the max palindrome.

"""

def reverse(x):
    """
    Reverse an integer x.

    """
    result = 0
    while x != 0:
        result *= 10
        result += x % 10
        x /= 10
    return result

def is_palindrome(x):
    """
    Determine whether integer x is palindromic.

    Check whether x reads the same forwards as backwards.
    Return true if it does, false otherwise.

    """
    return reverse(x) == x

max_palindrome = 0
for i in reversed(xrange(100, 1000)):
    if i * 999 <= max_palindrome: 
        break
    for j in reversed(xrange(i, 1000)):
        if i * j <= max_palindrome:
            break
        if is_palindrome(i * j):
            max_palindrome = i * j
print max_palindrome
