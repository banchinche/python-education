"""
Basic string operations.

Here I had to change source string to 'Strings are awesome' to
learn about basic string operations and correct printing information.
(spied on correct line ^_^)
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """

    source_str = "Strings are awesome!"
    # Length should be 20
    print('Length of s = %d' % len(source_str))

    # First occurrence of "a" should be at index 8
    print('The first occurrence of the letter a = %d' % source_str.index('a'))

    # Number of a's should be 2
    print('a occurs %d times' % source_str.count('a'))

    # Slicing the string into bits
    print('The first five characters are "%s"' % source_str[:5])        # Start to 5
    print('The next five characters are "%s"' % source_str[5:10])       # 5 to 10
    print('The thirteenth character is "%s"' % source_str[12])          # Just number 12
    print('The characters with odd index are "%s"' % source_str[1::2])  # (0-based indexing)
    print('The last five characters are "%s"' % source_str[-5:])        # 5th-from-last to end

    # Convert everything to uppercase
    print('String in uppercase: %s' % source_str.upper())

    # Convert everything to lowercase
    print('String in lowercase: %s' % source_str.lower())

    # Check how a string starts
    if source_str.startswith('Str'):
        print('String starts with "Str". Good!')

    # Check how a string ends
    if source_str.endswith('ome!'):
        print('String ends with "ome!". Good!')

    # Split the string into three separate strings,
    # each containing only a word
    print('Split the words of the string: %s' % source_str.split(' '))


if __name__ == '__main__':
    main()
