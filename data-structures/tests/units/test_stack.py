import pytest
from structures.stack import Stack


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], '4, 3, 2'),
                             ((2, 6, 9), '9, 6, 2'),
                             ([67, 98, 22], '22, 98, 67')
                         ])
def test_stack_init(given, expected):
    assert Stack(given).__str__() == expected


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], 3),
                             ((2, 6, 9, 20), 4),
                             ([67, 98, 22], 3)
                         ])
def test_len_stack(given, expected):
    assert len(Stack(given)) == expected


@pytest.mark.parametrize('given, peek',
                         [
                             ([44, 1, 6, 2, 22, 3], 3),
                             ((1, 6, 2, 3, 4, 8, 66), 66)
                         ])
def test_stack_peek(given, peek):
    stack = Stack(given)
    assert stack.peek().value == peek


@pytest.mark.parametrize('given, value, expected',
                         [
                             ([2, 4, 5], 22, '22, 5, 4, 2'),
                             ((7, 2, 9), 6, '6, 9, 2, 7')
                         ])
def test_stack_push(given, value, expected):
    stack = Stack(given)
    stack.push(value)
    assert stack.__str__() == expected


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 4, 5, 22], '5, 4, 2'),
                             ((7, 2, 9, 6), '9, 2, 7')
                         ])
def test_stack_push(given, expected):
    stack = Stack(given)
    assert stack.pop().value == given[-1]
    assert stack.__str__() == expected
