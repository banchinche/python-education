"""
Dictionaries task.

Here I had to:
- Add "Jake" to the phonebook with the phone number 938273443
- Remove Jill from the phonebook.
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """
    phonebook = {"John": 938477566,
                 "Jack": 938377264,
                 "Jill": 947662781
                 }

    # your code goes here
    phonebook['Jake'] = 938273443
    del phonebook["Jill"]

    # testing code
    if 'Jake' in phonebook:
        print('Jake is listed in the phonebook.')

    if "Jill" not in phonebook:
        print('Jill is not listed in the phonebook.')


if __name__ == '__main__':
    main()
