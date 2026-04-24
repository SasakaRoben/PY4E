"""
Write a program that reads the words in `words.txt` and stores them as keys in 
a dictionary. It doesn’t matter what the values are. 
Then you can use the `in` operator as a fast way to check whether a string is in the dictionary.

1. Create 2 lists of unique words from two different files
2. If the words in one list are more than the other list,:
    Trim the list of words with more words to be the same length as the other list
3. Create a dictionary with the words in the first list as keys and the words in the second list as values
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

