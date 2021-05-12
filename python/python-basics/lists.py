"""
Lists tasks.

Here I had to initialize numbers and strings lists with certain values
and also to fill in the variable second_name with the second name in the
names list, using the brackets operator [].
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """
    numbers = [1, 2, 3]
    strings = ['hello', 'world']
    names = ['John', 'Eric', 'Jessica']

    # write your code here
    second_name = names[1]

    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print('The second name on the names list is %s' % second_name)


if __name__ == '__main__':
    main()
