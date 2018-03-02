# Author: Deddryk

"""
Solution to problem 42.

Since the longest word in words.txt is only 14 characters,
this is easily solved by generating all triangle numbers less
than 26*14, then checking for each word value in that set.

"""

def word_value(word):
    value = 0
    for character in word:
        value += ord(character) - ord('A') + 1
    return value

def gen_triangle_numbers(max_num = 364):
    nums = set()
    step = 2
    cur_num = 1
    while cur_num <= 364:
        nums.add(cur_num)
        cur_num += step
        step += 1
    return nums

total = 0
triangle_nums = gen_triangle_numbers()
with open("solutions/problem42/words.txt") as file:
    words = [x[1:-1] for x in file.read().split(",")]
    for word in words:
        if word_value(word) in triangle_nums:
            total += 1
print total
