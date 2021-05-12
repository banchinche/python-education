"""
Conditions task.

Here I had to change the variables in the first section,
so that each if statement resolves as True.
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """

    # change this code
    number = 16
    second_number = 0
    first_array = [1, 1, 1]
    second_array = [1, 2]

    if number > 15:
        print('1')

    if first_array:
        print('2')

    if len(second_array) == 2:
        print('3')

    if len(first_array) + len(second_array) == 5:
        print('4')

    if first_array and first_array[0] == 1:
        print('5')

    if not second_number:
        print('6')


if __name__ == '__main__':
    main()
