import pytest
from software_testing.main import even_odd, sum_all, time_of_day, Product
from unittest.mock import patch


@pytest.mark.parametrize('number, expected',
                         [(1, 'odd'),
                          (10, 'even'),
                          (-4, 'even'),
                          (1.0, 'odd')])
def test_even_odd(number, expected):
    assert even_odd(number) == expected


def test_even_odd_another_type():
    number1 = None
    number2 = True
    number3 = list()
    number4 = tuple()
    with pytest.raises(TypeError):
        even_odd(number1)
        even_odd(number2)
        even_odd(number3)
        even_odd(number4)


@pytest.mark.parametrize('numbers, result_sum',
                         [((2, 3), 5),
                          ((1, 4), 5),
                          ([3, 4], 7)]
                         )
def test_sum_all(numbers, result_sum):
    assert sum_all(*numbers) == result_sum


def test_sum_all_another_type():
    numbers1 = ('1', '3')
    with pytest.raises(TypeError):
        sum_all(*numbers1)


def test_time_of_day_type():
    assert isinstance(time_of_day(), str)
    assert time_of_day() in ('night', 'morning', 'afternoon')


@patch(f'{__name__}.time_of_day', return_value='night')
def test_time_night(mock):
    assert mock() == 'night'


@patch(f'{__name__}.time_of_day', return_value='morning')
def test_time_morning(mock):
    assert mock() == 'morning'


@patch(f'__main__.time_of_day', return_value='afternoon', create=True)
def test_time_afternoon(mock):
    assert mock() == 'afternoon'


@pytest.mark.parametrize('parameters, expected',
                         [(('title1', 34.5, 5), ('title1', 34.5, 5)),
                          pytest.param(('title1', '34.5', 5), ('title1', 34.5, 5),
                                       marks=pytest.mark.xfail),
                          pytest.param(('title1', 34.5, '5'), ('title1', 34.5, 5),
                                       marks=pytest.mark.xfail)
                          ])
def test_product_init(parameters, expected):
    product = Product(*parameters)
    assert isinstance(product.title, str) and product.title == expected[0]
    assert isinstance(product.price, float) and product.price == expected[1]
    assert isinstance(product.quantity, int) and product.quantity == expected[2]


@pytest.mark.parametrize('to_subtract, expected',
                         [(2, 3),
                          (1, 4)])
def test_subtract_products(init_product, to_subtract, expected):
    product = init_product
    product.subtract_quantity(to_subtract)
    assert product.quantity == expected


@pytest.mark.parametrize('to_add, expected',
                         [(3, 8),
                          (1, 6)])
def test_add_products(init_product, to_add, expected):
    product = init_product
    product.add_quantity(to_add)
    assert product.quantity == expected


@pytest.mark.parametrize('new_price',
                         [22.12, 11.34, 45])
def test_change_price(init_product, new_price):
    product = init_product
    product.change_price(new_price)
    print(product.price, end='\n\n')
    print(product.price, end='\n\n')
    print(product.price, end='\n\n')
    assert product.price == new_price


def test_empty_shop_init(init_empty_shop):
    shop = init_empty_shop
    assert all([shop.money == 0., shop.products == []])


def test_product_shop_init(init_shop):
    shop = init_shop
    assert isinstance(shop.money, float) and shop.money == 0
    assert isinstance(shop.products, list)
    for product in shop.products:
        assert isinstance(product, Product)


@pytest.mark.parametrize('new_product',
                         [('title', 55.5, 5),
                          ('title', 55.5, 5)])
def test_add_product(init_empty_shop, new_product):
    shop = init_empty_shop
    product = Product(*new_product)
    shop.add_product(product)
    assert product in shop.products


@pytest.mark.parametrize('title, expected_index',
                         [('title5', 4),
                          ('title3', 2)])
def test_get_index(init_shop, title, expected_index):
    shop = init_shop
    assert shop._get_product_index(title) == expected_index


def test_get_index_none(init_shop):
    shop = init_shop
    none_title = 'not in the shop'
    assert shop._get_product_index(none_title) is None


@pytest.mark.parametrize('title, quantity, expected_receipt',
                         [('title5', 2, 111),
                          ('title3', 3, 166.5),
                          ('title4', 5, 277.5)
                          ])
def test_sell_product(init_shop, title, quantity, expected_receipt):
    shop = init_shop
    assert shop.sell_product(title, quantity) == expected_receipt
    if quantity == 5:
        with pytest.raises(TypeError):
            assert shop.products[shop._get_product_index(title)]
    else:
        with pytest.raises(ValueError):
            shop.sell_product(title, quantity + 5)


def test_sell_product_none(init_shop):
    shop = init_shop
    none_title = 'not in the shop'
    assert shop.sell_product(none_title, 4) is None
