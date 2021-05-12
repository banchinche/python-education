"""
String formatting task.

Here I had to write a format string which prints out the data using the
following syntax: 'Hello John Doe. Your current balance is $53.44.'
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """
    data = ('John', 'Doe', 53.44)
    format_string = 'Hello %s %s. Your current balance is $%s.'

    print(format_string % data)


if __name__ == '__main__':
    main()
