"""
Task with iterables
"""


class SentenceIterator:
    """
    Realizes IteratorProtocol
    """
    def __init__(self, sentence):
        self.__sentence = sentence
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
        if self.counter >= len(self.__sentence):
            raise StopIteration
        word = ''
        while self.counter < len(self.__sentence):
            char = self.__sentence[self.counter]
            if char not in ' !?.,:':
                word += char
            elif len(word) > 1:
                self.counter += 1
                if word != '':
                    return word
            else:
                word = ''
            self.counter += 1
        raise StopIteration


class Sentence:
    """
    Sentence class taken from given template
    """
    def __init__(self, text: str):
        """
        Initialization instance of the Sentence
        :param text: str
        """
        if not isinstance(text, str):
            raise TypeError
        if text[-1] not in ('.', '?', '!'):
            raise ValueError
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
        return SentenceIterator(self.__sentence)

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
        if self.counter >= len(self.__sentence):
            raise StopIteration
        word = ''
        while self.counter < len(self):
            char = self.__sentence[self.counter]
            if char not in ' !?.,:':
                word += char
            elif len(word) > 1:
                self.counter += 1
                yield word
                word = ''
            else:
                word = ''
            self.counter += 1

    @property
    def words(self):
        """
        Return list of the words in the sentence
        :return: list
        """
        return [word for word in self.__sentence.rstrip('!?.').split(' ') if len(word) > 1]

    @property
    def other_chars(self):
        """
        Returns list of the other chars in the sentence
        :return: list
        """
        return [word for word in self.__sentence.rstrip('!?.').split(' ') if len(word) == 1]


if __name__ == '__main__':
    s = Sentence('Let\'s dance f absolute d any f!')
    print(s)
    print(s._words())
    print(next(s._words()))
    print(s.words)
    print(s.other_chars)
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

