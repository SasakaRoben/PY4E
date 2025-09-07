"""
A simple program to simulate the operation of the Unix grep command.
1. Prompt the user for a regular expression
2. Count the number of lines that matched the regular expression
"""

import re
fname = 'mbox.txt'
fhand = open(fname)
count = 0
regex = input('Enter a regular expression: ')
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

print(fname, 'had', count, 'lines that matched', regex)
