"""
Module with recursive factorial realization
"""


def factorial(n: int) -> int:
    """
    Return the factorial of given n
    :param n: factorial argument
    :return: factorial of integer number
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
