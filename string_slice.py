str = 'X-DSPAM-Confidence: 0.8475'

colon_pos = str.find(':')
number = str[colon_pos + 1:]
number = float(number)
print(number)