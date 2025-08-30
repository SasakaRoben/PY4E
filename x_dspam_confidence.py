fname = './mbox-short.txt'
count = 0
total = 0.0
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        colon_pos = line.find(':')
        number = line[colon_pos + 1:]
        number = float(number)
        count = count + 1
        total = total + number