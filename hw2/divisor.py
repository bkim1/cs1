# author: Branden Kim
# assignment: 2
# description: Prints out all of the divisors of a given number


def get_divisor():
    num = int(input('Enter an integer number: '))
    return num, [str(i) for i in range(1, num // 2 + 1) if num % i == 0]


if __name__ == '__main__':
    num, divisors = get_divisor()

    print(f'Divisors of {num}:')
    print('\n'.join(divisors))
