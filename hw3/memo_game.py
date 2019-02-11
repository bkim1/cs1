# author: Branden Kim
# assignment: 3
# description: Program to play the Memorization Game


from time import sleep
from random import randint


class MemoGame():

    def __init__(self, difficulty=1, high_score=0):
        self.difficulty = difficulty
        self.high_score = high_score
        self.curr_nums = []

    def run(self):
        options = { 
            1: self.__set_difficulty,
            2: self.__start_game,
            3: None
        }
        user_input = self.__get_menu_input()
        while True:
            func = options.get(user_input)
            if func is None:
                break
            
            user_input = func()
        
        print('Thanks for playing the MEMOGAME')

    def __set_difficulty(self):
        while True:
            try:
                user_input = int(input('Enter a difficulty level (1-5): '))
            except ValueError:
                print('Value must be a number. Please try again.')
            except KeyboardInterrupt:
                print()
                break
            else:
                if user_input < 1 or user_input > 5:
                    print('Invalid difficulty. Please try again.')
                    continue
                self.difficulty = user_input
                return self.__get_menu_input()

    def __start_game(self):
        mistakes, score = 0, 0
        self.__generate_list()

        # Print numbers, wait for 10 seconds, and clear window
        print(f'- Level {self.difficulty} -')
        print('\n'.join([str(num) for num in self.curr_nums]))
        print('The round starts in 10 seconds')
        sleep(10)
        print('\n'.join(['' for _ in range(40)]))
        print('10 seconds up! Let the round begin!')

        # Start of round && user attempts
        for num in self.curr_nums:
            while mistakes < 2:
                try:
                    user_input = int(input('Enter the next number: '))
                except ValueError:
                    print('Incorrect!')
                    mistakes += 1
                else:
                    if num != user_input:
                        print('Incorrect number!')
                        mistakes += 1
                    else:
                        print('Correct!')
                        score += self.__get_points()
                        break
            else:
                print(f'Game over! Your points: {score}')
                break
        else:
            print(f'Congratulations! You win the round. Your points: {score}')

        if score > self.high_score:
            print('New high score!', end=' ')
            print(f'Old Score: {self.high_score}, New Score: {score}')
            self.high_score = score

        user_input = self.__print_end_of_round()
        if user_input == 2:
            return None
        
        return self.__get_menu_input()

    def __print_end_of_round(self):
        while True:
            try:
                user_input = int(input('Enter 1 to return to the main menu or 2 to exit: '))
            except ValueError:
                print('Value must be a number. Please try again.')
            else:
                if user_input < 1 or user_input > 2:
                    print('Invalid option. Please try again.')
                    continue
                return user_input

    def __get_menu_input(self):
        while True:
            try:
                self.__print_main_menu()
                user_input = int(input('Enter an option: '))
            except ValueError:
                print('Value must be a number. Please try again.')
            except KeyboardInterrupt:
                print()
                break
            else:
                if user_input < 1 or user_input > 3:
                    print('Invalid option. Please try again.')
                    continue
                return user_input

    def __generate_list(self):
        min_digits, max_digits = self.__get_word_lengths()
        round_length = self.__get_round_length()

        self.curr_nums = [randint(10**(min_digits-1), (10**max_digits) - 1) \
                          for _ in range(round_length)]

    def __get_word_lengths(self):
        return { 1: (2, 2), 2: (2, 2), 3: (2, 4),
                 4: (2, 4), 5: (3, 6) }.get(self.difficulty)

    def __get_round_length(self):
        return { 1: 5, 2: 7, 3: 9, 4: 11, 5: 14 }.get(self.difficulty)

    def __get_points(self):
        return self.difficulty * 10
    
    def __print_main_menu(self):
        print('\n========== MEMOGAME =========')
        print('||')
        print('| 1. Choose level of difficulty |')
        print('| 2. Start Game |')
        print('| 3. Exit the Game |')
        print('||')
        print(f'| Current Difficulty {self.difficulty}/5 |')
        print(f'| Highest score reached: {self.high_score} |')
        print('||')
        print('------------------------------------------')


if __name__ == '__main__':
    game = MemoGame()
    game.run()
