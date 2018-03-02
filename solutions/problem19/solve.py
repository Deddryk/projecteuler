# Author: Deddryk

"""
Solution to problem 19.

Loop through each month of each year, checking with python's 
calendar library what day of the week the first is.

"""

import calendar

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if calendar.weekday(year, month, 1) == calendar.SUNDAY:
            count += 1

print count
