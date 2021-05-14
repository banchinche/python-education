"""
Task with iterables
"""


class SentenceIterator:
    def __init__(self, words, sentence):
        self.__words = words
        self.__sentence = sentence
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
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
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError
        if text[-1] not in ('.', '?', '!'):
            raise ValueError
        self.__sentence = text
        self.counter = 0

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __len__(self):
        return len(self.__sentence)

    def __iter__(self):
        return SentenceIterator(self.words, self.__sentence)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return ' '.join(self.words[item])
        elif isinstance(item, int):
            if item >= len(self):
                raise IndexError('The index is out of range.')
            return self.words[item]
        else:
            raise TypeError('Invalid argument type.')

    def _words(self):
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
        return [word for word in self.__sentence.rstrip('!?.').split(' ') if len(word) > 1]

    @property
    def other_chars(self):
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

