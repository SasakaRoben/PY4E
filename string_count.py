def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

word = 'banana'
letter = 'a'
print("The letter ", letter, " appears ", count(word, letter), " times in the word ", word)