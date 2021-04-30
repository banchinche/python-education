"""
Modules and packages task.

Here I had to print an alphabetically sorted list of all
functions in the 're' module, which contain the word 'find'.
"""
import re


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """

    contain_find = [func for func in dir(re) if 'find' in func]
    print(sorted(contain_find))


if __name__ == '__main__':
    main()
