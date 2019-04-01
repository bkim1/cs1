# Author: Branden Kim
# Assignment: 5
# Description: Recursive GCD function


def gcd(first, second, curr_attempt):
    if second == 0:
        return first
    else:
        return gcd(second, first % second, first % second)


def main():
    while True:
        try:
            first = int(input('Please enter the first number: '))
        except ValueError:
            print('Only numbers greater than or equal to 1 are accepted as valid input.')
        else:
            if first >= 1:
                break
            else:
                print('Only numbers greater than or equal to 1 are accepted as valid input.')


    while True:
        try:
            second = int(input('Please enter the second number: '))
        except ValueError:
            print('Only numbers greater or than equal to 1 are accepted as valid input.')
        else:
            if second >= 1:
                break
            else:
                print('Only numbers greater than or equal to 1 are accepted as valid input.')


    print(f'The GCD for {first} and {second} is {gcd(first, second, second)}')


if __name__ == '__main__':
    main()
