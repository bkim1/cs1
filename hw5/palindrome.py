# Author: Branden Kim
# Assignment: 5
# Description: Recursive palindrome and reverse function


def palindrome(word):
    if not word:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palindrome(word[1:len(word) - 1])


def reverse(word):
    if len(word) == 1:
        return word
    else:
        return reverse(word[1:]) + word[0]


def main():
    word = input('Please enter a word to check if it is a palindrome: ')
    res = palindrome(word.lower())
    
    if res:
        print(f'The word {word} IS a palindrome.')
    else:
        print(f'The word {word} IS NOT a palindrome.')
        print(f'Backwards it becomes: {reverse(word)}')


if __name__ == '__main__':
    main()