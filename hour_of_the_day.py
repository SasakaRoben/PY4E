"""
This program counts the distribution of the hour of the day for each
 of the messages.
You can 
1. pull the hour from the “From” line by finding the time string 
2. split that string into parts using the colon character. 
3. Once you have accumulated the counts for each hour;
    print out the counts,one per line, sorted by hour as shown below.
      04 3
      06 1
      07 1
      09 2
      10 3
      11 6
      14 1
"""

hour_count = dict()
fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if (len(words) == 0) or (words[0] != 'From') or (len(words) < 6):
        continue
    time = words[5]
    hour = time.split(':')
    if len(hour) != 3:
        continue
    hour_count[hour[0]] = hour_count.get(hour[0], 0) + 1

hour_list = list(hour_count.items())
hour_list.sort()
for hour, count in hour_list:
    print(hour, count)

