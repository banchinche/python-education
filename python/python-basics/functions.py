"""
Functions task.

Here I had to:

-   Add a function named list_benefits() that returns
    the following list of strings: "More organized code",
    "More readable code", "Easier code reuse",
    "Allowing programmers to share and connect code together"

-   Add a function named build_sentence(info) which receives
    a single argument containing a string and returns a sentence
    starting with the given string and ending with the
    string " is a benefit of functions!"
"""


# Modify this function to return a list of strings as defined above
def list_benefits():
    """
    Just returns source list of benefits...
    :return: list of benefits
    """
    return ['More organized code',
            'More readable code',
            'Easier code reuse',
            'Allowing programmers to share and connect code together']


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    """
    Build sentence with certain benefit.
    :param benefit: one benefits from the source list
    :return: string-sentence contained benefit
    """
    return benefit + ' is a benefit of functions!'


def name_the_benefits_of_functions():
    """
    Prints all the function benefits.
    :return:
    """
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


if __name__ == '__main__':
    name_the_benefits_of_functions()
