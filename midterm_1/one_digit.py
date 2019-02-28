# Author: Branden Kim
# Description: Generates the sum of each digit of a number
#              if the number is greater than 9, then the
#              digits are added together again.
# 1b


def generate_digit(x):
    for ch in str(x):
        yield int(ch)


def one_digit(x):
    digit_sum = sum(i for i in generate_digit(x))

    while digit_sum > 9:
        digit_sum = sum(i for i in generate_digit(digit_sum))
    return digit_sum


if __name__ == '__main__':
    num = int(input('Enter a two-digit number: '))
    print(one_digit(num))
