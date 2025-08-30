names = ['Roben', 'Sasaka', 'Melody', 'Murengu', 'Moses', 'Muiga', 'Mutahi']
def chop(names):
    if len(names) > 1:
        del names[0]
        del names[-1]
    else:
        print('Chop Failed; list should have 2 or more elements')
    return None

