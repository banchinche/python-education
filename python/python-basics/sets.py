"""
Sets task.

Here I had to:
- Use the given lists to print out a set containing
all the participants from event A which did not attend event B.
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """

    a_names = ["Jake", "John", "Eric"]
    b_names = ["John", "Jill"]

    a_set = set(a_names)
    b_set = set(b_names)
    print(a_set.difference(b_set))


if __name__ == '__main__':
    main()
