names = ['Roben', 'Sasaka', 'Melody', 'Murengu', 'Moses', 'Muiga', 'Mutahi']
def chop(names):
    if len(names) > 1:
        del names[0]
        del names[-1]
    else:
        print('Chop Failed; list should have 2 or more elements')
    return None

def middle(names):
    if len(names) > 2:
        return names[1:-1]
    else:
        print('Middle Failed; list should have 3 or more elements')
        return None

print('Original List:', names)
chop(names)
print('After chop():', names)
names = ['Roben', 'Sasaka', 'Melody', 'Murengu', 'Moses', 'Muiga', 'Mutahi']
print('Original List:', names)
print('After middle():', middle(names))
