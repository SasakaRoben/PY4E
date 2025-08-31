"""
Write a program that reads the words in `words.txt` and stores them as keys in 
a dictionary. It doesn’t matter what the values are. 
Then you can use the `in` operator as a fast way to check whether a string is in the dictionary.

1. Create 2 lists of unique words from the file `words.txt` and `romeo.txt`
2. If the words in `romeo.txt` are more than the ones in `words.txt`:
    Trim the list of words in `romeo.txt` to be the same length as the list of words in `words.txt`
3. Create a dictionary with the words in `words.txt` as keys and the words in `romeo.txt` as values
"""
unique_keys = list()
unique_values = list()
word_dict = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_keys:
            unique_keys.append(word)

fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_values:
            unique_values.append(word)

if len(unique_values) > len(unique_keys):
    unique_values = unique_values[:len(unique_keys)]
else:
    unique_keys = unique_keys[:len(unique_values)]

for i in range(len(unique_keys)):
    word_dict[unique_keys[i]] = unique_values[i]

print(word_dict)

