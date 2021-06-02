import pytest
from software_testing.main import Product, Shop


@pytest.fixture
def init_product():
    return Product('title1', 34.5, 5)


@pytest.fixture(name='init_empty_shop')
def init_shop_no_products():
    return Shop(products=None)


@pytest.fixture(name='init_shop')
def init_shop_with_product():
    return Shop(products=[Product('title1', 55.5, 5), Product('title2', 55.5, 5),
                          Product('title3', 55.5, 5), Product('title4', 55.5, 5),
                          Product('title5', 55.5, 5), Product('title6', 55.5, 5)])
