# Author: Deddryk

"""
Solution to probelm 31

To solve this I used a recursive function num_ways that takes a list of
denominations and a value.  At each step, it uses as much of the highest
domination as it can without increasing the value, adding the number of
ways to make value - that total with the remaining denominations.  

"""

def num_ways(coins, value):
    if value == 0:
        return 1
    if len(coins) == 1:
        return 1
    total = 0
    ways = 0
    while(total <= value):
        ways += num_ways(coins[1:], value - total)
        total += coins[0]
    return ways
    

print num_ways([200, 100, 50, 20, 10, 5, 2, 1], 200)

