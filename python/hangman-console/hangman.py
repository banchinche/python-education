"""
Game settings module
"""
from generator import WordGenerator
from random import randrange
from typing import List


class Hangman:
    """
    Main class to operate with the generated word
    """
    def __init__(self, filename: str = 'history.txt'):
        """
        self.default_game is optional [1 - make word with certain first char,
        2 - with certain length of a word, 3 - with two first options above]
        """
        self.tries: int = 5
        self.history_filename: str = filename
        self.secret_word: str = str()
        self.current_word: str = '-'
        self.current_chars: List[str] = list()
        self.default_game: int = 1
        self.display = [
            '',
            '        $$$$$$$$$$$$$$$\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            ' $                          $\n',
            '        $$$$$$$$$$$$$$$\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        O             $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            ' $                          $\n',
            '        $$$$$$$$$$$$$$$\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        O             $\n'
            '      /   \\           $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            ' $                          $\n',
            '        $$$$$$$$$$$$$$$\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        O             $\n'
            '      / | \\           $\n'
            '        |             $\n'
            '                      $\n'
            '                      $\n'
            '                      $\n'
            ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            ' $                          $\n',
            '        $$$$$$$$$$$$$$$\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        |             $\n'
            '        O             $\n'
            '      / | \\           $\n'
            '        |             $\n'
            '       / \\            $\n'
            '                      $\n'
            '                      $\n'
            ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            ' $                          $\n'
        ]

    def load_previous_words(self):
        """
        Loads previous words from filename
        :return:
        """
        with open(self.history_filename, 'r') as f:
            words = f.readlines()
        return words

    def update_history_filename(self):
        """
        Updates history of previous words
        :return:
        """
        with open(self.history_filename, 'a') as f:
            f.write(self.secret_word + '\n')

    def generate_current_word(self, mode: int = 1, char: str = 'a', length: int = 0):
        """
        Generates secret word and current (using * and len of secret)
        :param mode: first char / length / char + len
        :param char: char option
        :param length: length option
        :return:
        """
        if length == 0:
            length = randrange(2, 10)
        if mode == 2:
            generator = WordGenerator()
            generator.generate_with_certain_len(length)
            self.secret_word = generator.word
        elif mode == 3:
            generator = WordGenerator()
            generator.generate_certain_first_len(char, length)
            self.secret_word = generator.word
        else:
            generator = WordGenerator()
            generator.generate_with_first_char(char)
            self.secret_word = generator.word
        self.current_word = '*' * len(self.secret_word)

    def attempt(self, attempt_str):
        """
        Attempt of guessing the word
        :param attempt_str: char or entire word string attempt
        :return:
        """
        if attempt_str != self.secret_word:
            if attempt_str in list(self.secret_word):
                self.current_chars.append(attempt_str)
            else:
                self.tries -= 1
            if ''.join(self.current_chars) == self.secret_word:
                return self.secret_word
        else:
            return self.current_word

    def show_current(self):
        """
        Generates view of current using already known chars and "*"
        :return:
        """
        word = ''
        for c in self.secret_word:
            if c in self.current_chars:
                word += c
            else:
                word += '*'
        self.current_word = word
        return self.current_word
