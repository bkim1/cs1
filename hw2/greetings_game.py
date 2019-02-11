# author: Branden Kim
# assignment: 2
# description: Get a random greeting for a user

import random


def get_greeting(name, low=0, high=24):
    rand_num = random.randint(low, high)
    print(rand_num)

    if rand_num >= 6 and rand_num <= 12:
        return f'Good morning, {name}!'
    elif rand_num > 12 and rand_num <= 15:
        return f'Good afternoon, {name}!'
    elif rand_num > 15 and rand_num <= 20:
        return f'Good evening, {name}!'
    else:
        return f'Good night, {name}!'


def greetings_game():
    name = input('What is your name? ')
    num_greetings = int(input('How many greetings do you want to see? '))

    for _ in range(num_greetings):
        print(get_greeting(name))


if __name__ == '__main__':
    greetings_game()
    