"""
Basic operators task.

Here I had to create two lists called x_list and y_list,
which contain 10 instances of the
variables x and y, respectively. Also required
to create a list called big_list,
which contains the variables x and y, 10 times each,
by concatenating the two lists you have created.
"""


def main():
    """
    Wrote a function just because pylint requires UPPER_CASE of variables in global scope.
    :return:
    """
    x_obj = object()
    y_obj = object()

    # need to do: change this code
    x_list = [x_obj] * 10
    y_list = [y_obj] * 10
    big_list = x_list + y_list

    print('x_list contains %d objects' % len(x_list))
    print('y_list contains %d objects' % len(y_list))
    print('big_list contains %d objects' % len(big_list))

    # testing code
    if x_list.count(x_obj) == 10 and y_list.count(y_obj) == 10:
        print('Almost there...')
    if big_list.count(x_obj) == 10 and big_list.count(y_obj) == 10:
        print('Great!')


if __name__ == '__main__':
    main()
