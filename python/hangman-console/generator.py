"""
Here is the class to generate word with certain options
"""
from random_words import RandomWords
WORDS = RandomWords()


class WordGenerator:
    """
    This class generates word with certain options
    (first char / len / char + len)
    """
    def __init__(self):
        """
        Initializing basic attributes of the word
        """
        self.word: str = ''
        self.word_len = 5

    def generate_with_first_char(self, char: str = 'a'):
        """
        Generates word with certain first char
        :param char: first char of the future word
        :return:
        """
        try:
            self.word = WORDS.random_word(char)
        except ValueError:
            pass

    def generate_with_certain_len(self, length: int = 0):
        """
        Generates word with certain length
        :param length: length of the word
        :return:
        """
        if length == 0:
            length = self.word_len
        temporary_word = WORDS.random_word()
        word_len = len(temporary_word)
        count = 0
        while word_len != length and count < 100000:
            temporary_word = WORDS.random_word()
            word_len = len(temporary_word)
            count += 1
        else:
            print('There is no word with such length and first char!')
            self.word = temporary_word

    def generate_certain_first_len(self, char: str = 'a', length: int = 0):
        """
        Generates word with first char and certain length
        :param char: first char of the word
        :param length: length of the word
        :return:
        """
        if length == 0:
            length = self.word_len
        temporary_word = WORDS.random_word(char)
        count = 0
        while count < 1e6:
            temporary_word = WORDS.random_word(char)
            word_len = len(temporary_word)
            count += 1
            if temporary_word[0] == char and word_len == length:
                self.word = temporary_word
                break
        else:
            print('There is no word with such length and first char!')
            self.word = temporary_word
