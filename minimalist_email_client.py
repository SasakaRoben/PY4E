"""
MBOX(mail box) is a popular file format to store and share a collection of emails.
This was used by early email servers and desktop apps. 
Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
Emails are separated by a special line which starts with From (notice the space). 
Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
Write a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

1. Write a program to read through the mail box data
2. When you find line that starts with “From”:
    1. Split the line into words using the split function. 
    2. We are interested in who sent the message, which is the second word on the From line.

        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    3. Parse the From line and print out the second word for each From line,
    4. Then you will also count the number of From (not From:) lines and print out a count at the end

This is a good sample output with a few lines removed:
    python fromcount.py
    Enter a file name: mbox-short.txt
    stephen.marquard@uct.ac.za
    [...some output removed...]
    cwen@iupui.edu
    There were 27 lines in the file with From as the first word

"""
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if (len(words) == 0) or (words[0] != 'From') or (len(words) < 3):
        continue
    print(words[1])
    count = count + 1
print('There were', count, 'lines in the file with From as the first word')