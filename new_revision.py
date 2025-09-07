"""
A program to look for the lines of the form:

New Revision: 39772

Extract the number from each of the lines
using a regular expression and the findall() method.
Compute the average of the numbers 
and print out the average as an integer.
"""

import re
fname = 'mbox.txt'
fhand = open(fname)
numbers = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('New Revision: ([0-9]+)', line)
    if len(stuff) != 1: continue
    number = int(stuff[0])
    numbers.append(number)

average = sum(numbers) / len(numbers)
print(int(average))