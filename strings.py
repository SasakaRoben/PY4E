# Exercise 1: Write a program that prints out the letters in a word backwards.
fruit = 'banana'
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1
