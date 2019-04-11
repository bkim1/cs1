# Author: Branden Kim
# Q2.A && Q3.B


def construct_food_dict(filename):
    food_pref = {}
    with open(filename, 'r') as f:
        for unstripped_line in f.readlines():
            line = unstripped_line.rstrip()
            name = line[: line.index(':')]
            food = line[line.index(':') + 1 : line.index('$')]
            pref = int(line[-1])

            if name in food_pref:
                food_pref[name].append([food, pref])
            else:
                food_pref[name] = [[food, pref]]
    
    return food_pref


def most_options(food_pref):
    max_person, max_options = '', 0
    for name in food_pref:
        if len(food_pref[name]) > max_options:
            max_options, max_person = len(food_pref[name]), name

    return (max_person, food_pref[max_person])



if __name__ == '__main__':
    food_pref = construct_food_dict('test.txt')
    print(f'Preferences: {food_pref}\n')
    print(f'Most Options: {most_options(food_pref)}')
