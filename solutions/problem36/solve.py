# Author: Deddryk

"""
Solution to problem 36

"""

def is_palindrome(string):
    return string == string[::-1]

sum_binary_and_decimal_palindromes = 0
for i in xrange(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        sum_binary_and_decimal_palindromes += i
print sum_binary_and_decimal_palindromes

