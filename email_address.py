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


address_list = list()
for email, count in address_count.items():
    address_list.append((count, email))

address_list.sort(reverse=True)
for count, email in address_list[:1]:
    print(email, count)

    
