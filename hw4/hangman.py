# Author: Branden Kim
# Assignment: 4
# Description: Hangman game

import sys
import tkinter as tk
from random import randint
from enum import Enum


#########################
#         MODEL         #
#########################


class RESULT(Enum):
    LOST = -2
    INCORRECT = -1
    GUESSED = 0
    CORRECT = 1
    WON = 2


class HangmanModel:
    
    def __init__(self, filename='Dictionary.txt'):
        # Load dictionary of words
        with open(filename, 'r') as f:
            self.words = [word.strip() for word in f.readlines()]

        # Get random word
        self.secret = self.words[randint(0, len(self.words) - 1)].upper()
        print(f'Model: {self.secret}')

        # Initialize other variables
        self.guessed = set()
        self.letter_positions = self.__find_positions(self.secret)
        self.current = ['_' for _ in range(len(self.secret))]
        self.incorrect = 0

    def guess_letter(self, letter):
        if letter in self.guessed:
            self.incorrect += 1
            return RESULT.GUESSED
        elif letter not in self.letter_positions:
            self.guessed.add(letter)
            self.incorrect += 1

            if self.incorrect == 5:
                return RESULT.LOST
            return RESULT.INCORRECT
        else:
            for i in self.letter_positions[letter]:
                self.current[i] = letter
            self.guessed.add(letter)

            if '_' not in self.current:
                return RESULT.WON
            return RESULT.CORRECT

    def reset_model(self):
        self.secret = self.words[randint(0, len(self.words) - 1)].upper()
        self.letter_positions = self.__find_positions(self.secret)
        self.current = ['_' for _ in range(len(self.secret))]
        self.guessed = set()
        self.incorrect = 0
        print(f'Model: {self.secret}\n')
        return True

    def __find_positions(self, word):
        """ Returns the indices of where each letter occurs """
        positions = {}

        for i, ch in enumerate(word):
            letter = ch.upper()
            positions[letter] = positions.get(letter, []) + [i]

        return positions


#########################
#          VIEW         #
#########################


class HangmanView:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.hangman_panel = HangmanPanel(self.root, self.controller)
        self.info_panel = InfoPanel(self.root, self.controller)

    def correct_guess(self):
        print('View: Correct!\n')
        self.info_panel.update_guessed(self.controller.get_used_words())
        self.info_panel.updated_current(self.controller.get_current_guess())

    def incorrect_guess(self):
        print('View: Incorrect!\n')
        self.info_panel.update_guessed(self.controller.get_used_words())
        self.hangman_panel.show_next()

    def guessed(self):
        print('View: Already Guessed!\n')
        self.info_panel.update_guessed(self.controller.get_used_words())
        self.info_panel.guessed()
        self.hangman_panel.show_next()

    def won(self):
        print('View: Won!\n')
        self.info_panel.update_guessed(self.controller.get_used_words())
        self.info_panel.updated_current(self.controller.get_current_guess())
        self.info_panel.won()

    def lost(self):
        print('View: Lost!\n')
        self.info_panel.lost(self.controller.get_secret_word())
        self.hangman_panel.show_next()

    def reset_game(self, guessed, current):
        print('View: Resetting UI!')
        self.info_panel.reset_game(guessed, current)
        self.hangman_panel.reset()


class HangmanPanel:

    def __init__(self, root, controller):
        self.controller = controller
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.TOP)

        # Draw Gallows
        main_beam = self.canvas.create_rectangle(
            10, 10, # (x1, y1)
            40, 410, # (x2, y2)
            fill='#9e001c')
        support_beam = self.canvas.create_polygon(
            40, 50, # top leftside corner (x, y)
            40, 70, # bottom leftside corner (x, y)
            90, 10, # bottom rightside corner (x, y)
            70, 10, # top rightside corner (x, y)
            fill='#9e001c')
        top_beam = self.canvas.create_rectangle(10, 10, 175, 30,
            fill='#9e001c')
        rope = self.canvas.create_rectangle(140, 30, 143, 75,
            fill='#a5692c', outline='')
        noose = self.canvas.create_oval(
            133, 75, # (x1, y1) top left corner
            150, 92, # (x2, y2) bottom right corner
            width=2, outline='#a5692c')

        # Draw Person
        head = self.canvas.create_oval(128, 45, 155, 72,
            fill='black', state='hidden')
        torso = self.canvas.create_rectangle(140, 72, 143, 132,
            fill='black', state='hidden')
        arms = self.canvas.create_rectangle(100, 100, 180, 103,
            fill='black', state='hidden')
        left_leg = self.canvas.create_polygon(
            140, 128, 140, 133,
            100, 155, 100, 150,
            fill='black', state='hidden')
        right_leg = self.canvas.create_polygon(
            143, 128, 143, 133,
            180, 155, 180, 150,
            fill='black', state='hidden')

        self.body = [head, torso, arms, left_leg, right_leg]
        self.body_counter = 0

    def show_next(self):
        self.canvas.itemconfig(self.body[self.body_counter], state='normal')
        self.body_counter += 1

    def reset(self):
        for limb in self.body:
            self.canvas.itemconfig(limb, state='hidden')
        self.body_counter = 0
        

class InfoPanel:

    def __init__(self, root, controller):
        self.controller = controller
        self.panel = tk.Frame(root)
        self.panel.pack(side=tk.BOTTOM)

        # Entry Frame and label/entry
        self.entry_frame = tk.Frame(self.panel)
        self.entry_frame.pack(side=tk.TOP)

        self.entry_label = tk.Label(self.entry_frame, text='Enter a letter: ')
        self.entry_label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.entry_frame, width=1)
        self.entry.pack(side=tk.RIGHT)
        self.entry.bind('<Return>', self.on_enter)

        # Used words and current words label
        self.info_frame = tk.Frame(self.panel)
        self.info_frame.pack(side=tk.TOP)

        self.used_label = tk.Label(self.info_frame,
            text=f'Letters Played: {" ".join(self.controller.get_used_words())}')
        self.used_label.pack()

        self.current_word_label = tk.Label(self.info_frame,
            text=f'Word: {" ".join(self.controller.get_current_guess())}')
        self.current_word_label.pack()

        # Extra messages and reset button init
        self.message = tk.Label(self.info_frame, font=('Helvitica', 14,'bold'))
        self.message.pack()

        self.reset = tk.Button(self.info_frame, text='Play Again',
            command=self.controller.reset_game)
        self.reset.pack()
        self.reset.pack_forget()

    def on_enter(self, event=None):
        letter = self.entry.get()
        if len(letter) > 1:
            self.message.config(text='Entered too many characters. Try again.')
            self.panel.after(5000, self.__clear_message)
        else:
            try:
                int(letter)
            except ValueError:
                self.controller.make_guess(letter.upper())
            else:
                self.message.config(text='No numbers allowed. Only characters.')
                self.panel.after(5000, self.__clear_message)

        self.__clear_entry()

    def guessed(self):
        self.message.config(text='Letter already guessed. Penalty.')
        self.panel.after(5000, self.__clear_message)

    def update_guessed(self, guessed):
        self.used_label.config(text=f'Letters Played: {" ".join(guessed)}')

    def updated_current(self, current):
        self.current_word_label.config(text=f'Word: {" ".join(current)}')

    def won(self):
        self.message.config(text='Congratulations! You won!')
        self.__show_reset_button()

    def lost(self, secret):
        self.message.config(text='RIP. You lost!')
        self.updated_current(list(secret))
        self.__show_reset_button()

    def reset_game(self, guessed, current):
        self.update_guessed(guessed)
        self.updated_current(current)
        self.__clear_message()
        self.reset.pack_forget()

    def __show_reset_button(self):
        self.reset.pack()

    def __clear_entry(self, event=None):
        self.entry.delete(0, 'end')

    def __clear_message(self, event=None):
        self.message.config(text='')


#########################
#       CONTROLLER      #
#########################


class HangmanController:

    def __init__(self, filename='Dictionary.txt'):
        self.root = tk.Tk()
        self.model = HangmanModel(filename)
        self.view = HangmanView(self.root, self)

    def run(self):
        self.root.title('Hangman')
        self.root.mainloop()

    def get_used_words(self):
        return self.model.guessed

    def get_current_guess(self):
        return self.model.current

    def get_secret_word(self):
        return self.model.secret

    def make_guess(self, letter):
        cases = {
            RESULT.GUESSED: self.view.guessed,
            RESULT.INCORRECT: self.view.incorrect_guess,
            RESULT.CORRECT: self.view.correct_guess,
            RESULT.WON: self.view.won,
            RESULT.LOST: self.view.lost
        }
        return cases.get(self.model.guess_letter(letter))()

    def reset_game(self, event=None):
        self.model.reset_model()
        self.view.reset_game(self.get_used_words(), self.get_current_guess())


if __name__ == '__main__':
    if len(sys.argv) == 1:
        controller = HangmanController()
    else:
        controller = HangmanController(sys.argv[1])

    controller.run()
