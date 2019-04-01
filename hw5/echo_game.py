# Author: Branden Kim
# Assignment: 5
# Description: Recursive function to print out the echoes of a sentence


def echo_game(word, fraction, num_echoes):
    if len(word) > 1:
        echo_len = len(word) - int(len(word) * fraction)
        print(word)
        return echo_game(word[echo_len:], fraction, num_echoes + 1)
    else:
        print(f'Total number of echoes: {num_echoes}')


def main():
    while True:
        try:
            fraction = float(input('Enter the fraction: '))
        except ValueError:
            print('Your number must be a fraction (in decimal form).')
        else:
            if fraction >= 0 and fraction < 1:
                break
            else:
                print('Your number must be a fraction (in decimal form).')

    word = input('Enter the sentence: ')
    echo_game(word, fraction, 0)


if __name__ == '__main__':
    main()
