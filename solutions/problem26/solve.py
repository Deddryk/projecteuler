# Author: Deddryk
"""
Solution to Project Euler problem 26.

I'm sure there is a more elegant solution to this but I basically hacked
out the elementary school learned long division in python and performed
1 / x for x in 2 to 999, saving the divisor that produced the longest
repeating decimal.

Runs in about .1 seconds on my system.

"""

def one_div(divisor):
    """
    Perform long division of 1 / divisor where divisor is an integer.

    Essentially, perform the elementary school algorithm for long
    division on 1 / divisor.

    Return a dictionary with two keys: 'len' the period of the decimal
    repeat.  And 'result': a list containing the sequence of integers
    that make up the decimal notation of the resulting number

    """

    # Used to improve performance of used numerators lookup
    used_numerators = set()
    # Needed to quickly find the period of a repeat
    used_numerators_list = []
    result = []
    numerator = 10
    while numerator != 0 and numerator not in used_numerators:
        used_numerators.add(numerator)
        used_numerators_list.append(numerator)
        while numerator / divisor == 0:
            result.append(0)
            numerator *= 10
            used_numerators.add(numerator)
            used_numerators_list.append(numerator)
        result.append(numerator / divisor)
        numerator = (numerator - numerator / divisor * divisor) * 10
    if numerator == 0:
        return {'len': 0, 'result': result}
    else:
        return {
            'len': len(used_numerators_list) - 
            used_numerators_list.index(numerator), 
            'result': result}


max_repeat = 0
divisor = 0
for i in xrange(1, 1000):
    decimal_rep = one_div(i)
    if (decimal_rep['len'] > max_repeat):
        max_repeat = decimal_rep['len']
        divisor = i
print divisor
