fname = './mbox-short.txt'
count = 0
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'): 