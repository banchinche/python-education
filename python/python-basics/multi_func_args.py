"""
Multiple function arguments task.

Here I had to:

-   Fill in the foo and bar functions so they can receive a variable
    amount of arguments (3 or more).
-   The foo function must return the amount of extra arguments received.
-   The bar must return True if the argument with the keyword
    magic_number is worth 7, and False otherwise.
"""


# edit the functions prototype and implementation
def foo_function(a_parameter, b_parameter, c_parameter, *args):
    """
    Returns amount of received arguments
    :param a_parameter: unusable
    :param b_parameter: unusable
    :param c_parameter: unusable
    :param args:
    :return:
    """
    return len(args)


def bar_function(a_parameter, b_parameter, c_parameter, **kwargs):
    """
    Returns is the magic_number worth 7.
    :param a_parameter: unusable
    :param b_parameter: unusable
    :param c_parameter: unusable
    :param kwargs:
    :return:
    """
    return kwargs['magic_number'] == 7


# test code
if __name__ == '__main__':
    if foo_function(1, 2, 3, 4) == 1:
        print('Good.')
    if foo_function(1, 2, 3, 4, 5) == 2:
        print('Better.')
    if not bar_function(1, 2, 3, magic_number=6):
        print("Great.")
    if bar_function(1, 2, 3, magic_number=7):
        print("Awesome!")
