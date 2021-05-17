"""
Task with iterables
"""
from string import ascii_letters as letters


class SentenceIterator:
    """
    Realizes IteratorProtocol
    """
    def __init__(self, words):
        self.words = words
        self.counter = 0

    def __iter__(self):
        """
        Iter magic method realization for IteratorProtocol
        :return: instance itself
        """
        return self

    def __next__(self):
        """
        Next magic method realization for IteratorProtocol
        :return: str
        """
        if self.counter >= len(self.words):
            raise StopIteration
        while self.counter < len(self.words):
            word = self.words[self.counter]
            self.counter += 1
            return word


class Sentence:
    """
    Sentence class taken from given template
    """
    excluding = ' ()/\\\'"!?.,:'

    def __init__(self, text: str):
        """
        Initialization instance of the Sentence
        :param text: str
        """
        if not isinstance(text, str):
            raise TypeError('Enter just strings!')
        if text[-1] not in '.?!':
            raise ValueError('Sentence must be completed (ends with !/?/.)')
        self.__sentence = text

        self.counter = 0

    def __repr__(self):
        """
        String representation of the instance
        :return: str
        """
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __len__(self):
        """
        Return length of the sentence
        :return:
        """
        return len(self.__sentence)

    def __iter__(self):
        """
        Returns iterator object - SentenceIterator
        :return:
        """
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        """
        Slicing and indexing to take words from the words list (w/o other chars!)
        :param item: index or slice
        :return: str
        """
        if isinstance(item, slice):
            return ' '.join(self.words[item])
        elif isinstance(item, int):
            if item >= len(self):
                raise IndexError('The index is out of range.')
            return self.words[item]
        else:
            raise TypeError('Invalid argument type.')

    def _words(self):
        """
        Return lazy iterator (just words without other chars!)
        :return: iterator
        """
        word = ''
        while self.counter < len(self):
            char = self.__sentence[self.counter]
            if char not in self.excluding:
                word += char
            elif len(word) > 1:
                self.counter += 1
                yield word
                word = ''
            else:
                word = ''
            self.counter += 1
        self.counter = 0

    @property
    def words(self):
        """
        Return list of the words in the sentence
        :return: list
        """
        return [word.strip(self.excluding) for word in self.__sentence.rstrip('!?.').split(' ') if len(word) > 1]

    @property
    def other_chars(self):
        """
        Returns list of the other chars in the sentence
        :return: list
        """
        return [char for char in self.__sentence if char not in letters and char != ' ']


if __name__ == '__main__':
    s = Sentence('There is another statement (rule, point).')
    print(s._words())
    print(s)
    print(s.words)
    print(s.other_chars)
    print(next(s._words()))
    print(next(s._words()))
    print(next(s._words()))
    print(next(s._words()))
    print(next(s._words()))
    print(next(s._words()))
    print(list(s._words()))
    print(s[-1])
    print(s[0])
    print(s[1:3])
    print('\nFor loop iteration:')
    for _word in s:
        print(_word)
    print('\nCreating SentenceIterator instance:')
    sentence_iterator = iter(s)
    print(sentence_iterator)
    print(next(sentence_iterator))
    print(next(sentence_iterator))

    print('\nCreating another Sentence instance for check zeroing self.counter...')
    f = Sentence('There is another.')
    print('Counter:', f.counter)
    print(next(f._words()))
    print(next(f._words()))
    print(f.words)
