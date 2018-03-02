# Author: Deddryk

"""
Solution to problem 22

"""

def alphabetic_value(string):
    s = 0
    for char in string:
        s += ord(char) - ord('A') + 1
    return s

total_value = 0
with open("solutions/problem22/names.txt") as name_file:
    names = [x[1:-1] for x in name_file.read().split(',')]
    for i, name in enumerate(sorted(names)):
        total_value += alphabetic_value(name) * (i + 1)
print total_value


