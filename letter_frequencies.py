"""
A program that reads a file and prints the letters
in decreasing order of frequency.
The program should convert all the input to lower case
and only count the letters a-z.
It should not count spaces, digits, punctuation, or 
anything other than the letters a-z.
Find text samples from several different languages
and see how letter frequency varies between languages.
Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies
"""

import string
fhand = open('romeo-full.txt')
letter_counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    for char in line:
        if char in string.ascii_lowercase:
            letter_counts[char] = letter_counts.get(char, 0) + 1

letter_list = list()
for letter, count in letter_counts.items():
    letter_list.append((count, letter))

letter_list.sort(reverse=True)
for count, letter in letter_list:
    print(letter, count)
    