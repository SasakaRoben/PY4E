count = 0
total = 0.0
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        colon_pos = line.find(':')
        number = line[colon_pos + 1:]
        number = float(number)
        count = count + 1
        total = total + number

print('Average spam confidence:', total / count)