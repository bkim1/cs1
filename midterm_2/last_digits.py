# Author: Branden Kim
# Q1.B


def last_digits(digits, length):
    if len(str(digits)) != length:
        return digits
    else:
        return last_digits(int(str(digits)[1:]), length)


if __name__ == '__main__':
    num = int(input('Enter an integer number: '))
    print(last_digits(num, len(str(num))))
