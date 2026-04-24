"""
List all unique words, 
sorted in alphabetical order, 
that are stored in a file 'romeo.txt', which contains a subset of Shakespeare’s work.

1. Create a list of unique words, which will contain the final result. 
2. Write a program to open the file 'romeo.txt' and read it line by line. 
3. For each line, split the line into a list of words using the 'split' function. 
4. For each word, check to see if the word is already in the list of unique words. 
5. If the word is not in the list of unique words, add it to the list. 
6. When the program completes, sort and print the list of unique words in alphabetical order

"""
unique_words = list()
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
print(unique_words)