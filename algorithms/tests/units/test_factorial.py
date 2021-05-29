import pytest
from algorithms.factorial import factorial


@pytest.mark.parametrize('number, expected',
                         [(1, 1),
                          (5, 120),
                          (6, 720),
                          pytest.param('3', 6,
                                       marks=pytest.mark.xfail),
                          pytest.param(5, '120',
                                       marks=pytest.mark.xfail)
                          ])
def test_factorial(number, expected):
    assert type(factorial(number)) == int
    assert factorial(number) == expected
