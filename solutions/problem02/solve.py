# Author: Deddryk
"""
Solution to project euler problem 2

It is easy to see that every third term in the Fibonacci sequence is
even.
1, 1, 2, 3, 5, 8, ...
odd + odd = even, odd + even = odd, even + odd = odd, odd + odd = even
Let's try to get a relation for every third Fibonacci term.
fib(i) = fib(i - 1) + fib(i - 2)
       = fib(i - 3) + 2fib(i - 2)
       = fib(i - 3) + 2(fib(i - 3) + fib(i-4)
       = 3fib(i - 3) + 2fib(i - 4)
       = 3fib(i - 3) + fib(i - 4) + fib(i - 5) + fib(i - 6)
       = 4fib(i - 3) + fib(i - 6)
Now we can consider only the even terms in our calculations.

"""

current_fib_term = 8
prev_fib_term = 2
sum = 2
while current_fib_term < 4000000:
    sum += current_fib_term
    temp = prev_fib_term
    prev_fib_term = current_fib_term
    current_fib_term = 4 * current_fib_term + temp
print sum
