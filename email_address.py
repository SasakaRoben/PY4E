"""
A program that:
1. Reads through a mail log
2. Builds a histogram using a dictionary to count how many messages have come from each email address
3. Prints the dictionary.
4. Find the most prolific committer by looking through the dictionary using a maximum loop
"""
address_count = dict()
fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if (len(words) == 0) or (words[0] != 'From') or (len(words) < 2):
        continue
    address_count[words[1]] = address_count.get(words[1], 0) + 1

print(address_count)

biggest = None
big_address = None
keys_list = list(address_count.keys())
for key in keys_list:
    if biggest is None or address_count[key] > biggest:
        biggest = address_count[key]
        big_address = key

print(big_address, biggest)
