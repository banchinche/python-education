import pytest
from structures.queue import Queue


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], '2, 3, 4'),
                             ((2, 6, 9), '2, 6, 9'),
                             ([67, 98, 22], '67, 98, 22')
                         ])
def test_queue_init(given, expected):
    assert Queue(given).__str__() == expected


@pytest.mark.parametrize('given, expected',
                         [
                             ([2, 3, 4], 3),
                             ((2, 6, 9, 20), 4),
                             ([67, 98, 22], 3)
                         ])
def test_len_queue(given, expected):
    assert len(Queue(given)) == expected


@pytest.mark.parametrize('given, value, expected',
                         [
                             ([2, 3, 4], 5, '2, 3, 4, 5'),
                             ((67, 98, 22), 7, '67, 98, 22, 7')
                         ])
def test_queue_enqueue(given, value, expected):
    queue = Queue(given)
    queue.enqueue(value)
    assert queue.__str__() == expected


@pytest.mark.parametrize('given, expected',
                         [
                             ([67, 98, 22, 7], '98, 22, 7'),
                             ((2, 3, 4, 5), '3, 4, 5')
                         ])
def test_queue_dequeue(given, expected):
    queue = Queue(given)
    queue.dequeue()
    assert queue.__str__() == expected


@pytest.mark.parametrize('given, peek',
                         [
                             ([44, 1, 6, 2, 22, 3], 44),
                             ((1, 6, 2, 3, 4, 8, 66), 1)
                         ])
def test_queue_peek(given, peek):
    queue = Queue(given)
    assert queue.peek().value == peek
