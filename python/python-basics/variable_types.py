"""
Variables and types exercise.

Here I had to declare 3 variables with certain values and print them.
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """
    # change this code
    my_string = 'hello'
    my_float = 10.
    my_int = 20

    # testing code
    if my_string == 'hello':
        print('String: %s' % my_string)
    if isinstance(my_float, float) and my_float == 10.0:
        print('Float: %f' % my_float)
    if isinstance(my_int, int) and my_int == 20:
        print('Integer: %d' % my_int)


if __name__ == '__main__':
    main()
