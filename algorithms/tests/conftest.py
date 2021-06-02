import pytest
from random import sample


@pytest.fixture
def create_set():
    test_set = list()
    for i in range(10):
        generated = sample(range(20, 90), 6)
        test_set.append(generated)
    return test_set
