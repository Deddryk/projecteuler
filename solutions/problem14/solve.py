#Author: Deddryk

"""
Solution for problem 14.


"""

class Hailstone(object):
    """
    Hailstone represents a number in a Collatz sequence
   
    Each member of the sequence has its associated number,
    the following Hailstone object, and the length of the
    sequence if it started at this point.
    
    """

    def __init__(self, num, next_stone, length):
        self.num = num
        self.next_stone = next_stone
        self.length = length

used_nums = {1: Hailstone(1, None, 1)}
max_seq = 1

def generate_sequence(n):
    if n in used_nums:
        return used_nums[n]
    next_stone = generate_sequence(n / 2 if n % 2 == 0 else 3 * n + 1)
    used_nums[n] = Hailstone(n, next_stone, next_stone.length + 1)
    return used_nums[n]

max_sequence = 1
max_start = 1
for i in xrange(2, 1000000):
    n = generate_sequence(i)
    if n.length > max_sequence:
        max_sequence = n.length
        max_start = n.num
print max_start, max_sequence
