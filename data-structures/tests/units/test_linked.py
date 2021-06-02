import pytest
from structures.linked_list import LinkedList


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], '2, 3, 4'),
                             ((2, 6, 9), '2, 6, 9')
                         ])
def test_linked_init(given, expected):
    assert LinkedList(given).__str__() == expected


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], 3),
                             ((2, 6, 9, 20), 4)
                         ])
def test_len_linked(given, expected):
    assert len(LinkedList(given)) == expected


@pytest.mark.parametrize('given, value, expected',
                         [
                             ([2, 3, 4], 5, '2, 3, 4, 5'),
                             ((2, 6, 9), 20, '2, 6, 9, 20')
                         ])
def test_linked_append(given, value, expected):
    linked = LinkedList(given)
    linked.append(value)
    assert linked.__str__() == expected


@pytest.mark.parametrize('given, value, expected',
                         [
                             ([2, 3, 4], 5, '5, 2, 3, 4'),
                             ((2, 6, 9), 20, '20, 2, 6, 9')
                         ])
def test_linked_prepend(given, value, expected):
    linked = LinkedList(given)
    linked.prepend(value)
    assert linked.__str__() == expected


@pytest.mark.parametrize('given, value, index, expected',
                         [
                             ([1, 6, 2, 3, 4, 8], 22, 3, '1, 6, 2, 22, 3, 4, 8'),
                             ((1, 6, 2, 22, 3, 4, 8), 44, 0,  '44, 1, 6, 2, 22, 3, 4, 8')
                         ])
def test_linked_insert(given, value, index, expected):
    linked = LinkedList(given)
    linked.insert(value, index)
    assert linked.__str__() == expected


@pytest.mark.parametrize('given, index, expected',
                         [
                             ([44, 1, 6, 2, 22, 3], 0, '1, 6, 2, 22, 3'),
                             ((1, 6, 2, 3, 4, 8, 66), 6,  '1, 6, 2, 3, 4, 8')
                         ])
def test_linked_delete(given , index, expected):
    linked = LinkedList(given)
    linked.delete(index)
    assert linked.__str__() == expected


@pytest.mark.parametrize('given, head, tail',
                         [
                             ([44, 1, 6, 2, 22, 3], 44, 3),
                             ((1, 6, 2, 3, 4, 8, 66), 1, 66)
                         ])
def test_linked_head_tail(given, head, tail):
    linked = LinkedList(given)
    assert linked.head.value == head
    assert linked.tail.value == tail
