"""
This program records the domain name (instead of the address) 
where the message was sent from 
instead of who the mail came from (i.e., the whole email address).
"""

domain_count = dict()
fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if (len(words) == 0) or (words[0] != 'From') or (len(words) < 2):
        continue
    domain = words[1].split('@')
    if len(domain) != 2:
        continue
    domain_count[domain[1]] = domain_count.get(domain[1], 0) + 1

print(domain_count)