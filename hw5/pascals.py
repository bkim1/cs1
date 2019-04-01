# Author: Branden Kim
# Assignment: 5
# Description: Recursive function to print out pascal's triangle


def pascals(cur_level, num_levels, level_list):
    if cur_level > num_levels:
        return level_list
    elif cur_level == 0:
        level_list.append([1])
    elif cur_level == 1:
        level_list.append([1, 1])
    else:
        temp, prev_list = [1], level_list[cur_level - 1]

        for i in range(1, len(prev_list)):
            temp.append(prev_list[i] + prev_list[i - 1])
        
        temp.append(1)
        level_list.append(temp)

    return pascals(cur_level + 1, num_levels, level_list)

def main():
    print("Welcome to the Pascal's triangle generator.")
    while True:
        try:
            num_levels = int(input('Please enter the number of levels to generate: '))
        except ValueError:
            print('Your number must be positive (greater than zero).')
        else:
            if num_levels >= 1:
                break
            else:
                print('Your number must be positive (greater than zero).')

    res = pascals(0, num_levels, [])

    for level in res:
        print(' '.join((str(i) for i in level)))


if __name__ == '__main__':
    main()
