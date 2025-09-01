"""
A program that categorizes each mail message by the day of the week the commit was done.

1. Look for lines that start with "From ".
2. Look for the third word 
3. Keep a running count of each day of the week.
4. Print out the contents of your dictionary (order does not matter).   
"""
days_list = list()
days_dict = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if (len(words) == 0) or (words[0] != 'From') or (len(words) < 3):
        continue
    days_list.append(words[2])

for day in days_list:
    days_dict[day] = days_dict.get(day, 0) + 1

print(days_dict)


    