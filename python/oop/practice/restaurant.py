"""
Restaurant application structure
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice, randrange, uniform
from typing import Union


class Equipment:
    """
    Equipment for waiters and cooks, number of them depends on equipment count
    """
    def __init__(self, cooks: int = 0, waiters: int = 0):
        """
        Sets number of the equipment for waiters and cooks
        :param cooks: int
        :param waiters: int
        """
        self.cook_equip = {'uniform': cooks,
                           'kitchen-tools': cooks}
        self.waiter_equip = {'uniform': waiters,
                             'waiter-tools': waiters}
        # print('Equipment counted at the start of the day.')


class Cook(ABC):
    """
    Protocol (Abstract class) to define abstract methods of the cook,
    for responsibility-chain pattern
    """
    cooks = Equipment(cooks=4)
    dishes = {
        'chef': ('chef1', 'chef2', 'chef3'),
        'confectioner': ('con1', 'con2', 'con3'),
        'meat-cook': ('meat1', 'meat2', 'meat3'),
        'fish-cook': ('fish1', 'fish2', 'fish3')
    }

    @abstractmethod
    def set_next(self, cook):
        """
        Sets next cook if current one can't cook the dish
        :param cook: Cook
        :return:
        """

    @abstractmethod
    def cook(self, dish):
        """
        Cooks the dish
        :param dish: str
        :return:
        """


class AbstractCook(Cook):
    """
    Realizes chain process
    """
    _next_cook = None

    def set_next(self, cook):
        """
        Sets next cook if current one can't cook the dish
        :param cook: AbstractCook
        :return:
        """
        self._next_cook = cook
        return cook

    @abstractmethod
    def cook(self, dish):
        """
        Cooks the dish
        :param dish: str
        :return: next cook or None
        """
        if self._next_cook.cook:
            return self._next_cook.cook(dish)
        return None


class Chef(AbstractCook):
    """
    Realizes cooking for Chef-cook
    """
    def cook(self, dish: str):
        """
        Cooks the dish
        :param dish: str
        :return: str or next cook
        """
        if dish in Cook.dishes['chef']:
            return 'Cooked by Chef!'
        return super().cook(dish)


class Confectioner(AbstractCook):
    """
    Realizes cooking for Confectioner-cook
    """
    def cook(self, dish: str):
        """
        Cooks the dish
        :param dish: str
        :return: str or next cook
        """
        if dish in Cook.dishes['confectioner']:
            return 'Cooked by Confectioner!'
        return super().cook(dish)


class MeatCook(AbstractCook):
    """
    Realizes cooking for Meat-cook
    """
    def cook(self, dish: str):
        """
        Cooks the dish
        :param dish: str
        :return: str or next cook
        """
        if dish in Cook.dishes['meat-cook']:
            return 'Cooked by Meat-Cook!'
        return super().cook(dish)


class FishCook(AbstractCook):
    """
    Realizes cooking for Fish-cook
    """
    def cook(self, dish: str):
        """
        Cooks the dish
        :param dish: str
        :return: str or next cook
        """
        if dish in Cook.dishes['fish-cook']:
            return 'Cooked by Fish-Cook!'
        return super().cook(dish)


class Order:
    """
    Order class that represents menu values and calculating amount process
    """
    __totals = 0
    menu = {
        'chef1': 42.5,
        'chef2': 43.5,
        'chef3': 44.5,
        'con1': 14.5,
        'con2': 15.5,
        'con3': 16.5,
        'meat1': 11.5,
        'meat2': 12.5,
        'meat3': 13.5,
        'fish1': 32.5,
        'fish2': 33.5,
        'fish3': 34.5
    }

    def __init__(self, wish: Union[list, str]):
        """
        Calculating amount of the order if dish in menu
        :param wish: it could be single dish or several
        """
        self.__number: int = self.__totals + 1
        self.__increment_totals()
        self.dishes: list = []
        self.__amount: float = 0.
        if isinstance(wish, list):
            for dish in wish:
                if dish in list(self.menu.keys()):
                    self.dishes.append(dish)
                    self.__amount += self.menu[dish]
        else:
            if wish in list(self.menu.keys()):
                self.dishes.append(wish)
                self.__amount += self.menu[wish]
        print('Order was made and delivered to kitchen!')

    @classmethod
    def __increment_totals(cls):
        """
        Class method to increment total number of orders
        :return: int
        """
        cls.__totals += 1

    @property
    def number(self):
        """
        Property to return number of the certain order
        :return: int
        """
        return self.__number

    @property
    def amount(self):
        """
        Property to return amount of the certain order
        :return: float
        """
        return self.__amount


class Waiter:
    """
    Waiter class realizes accepting order and gaining bonus tips for restaurant
    """
    waiter_names = ('John', 'Helen', 'Rick', 'Morty')
    waiters = Equipment(waiters=2)

    def __init__(self):
        """
        Initializing one waiter with random name
        """
        self.name: str = choice(self.waiter_names)
        self.__tips: float = 0.

    def accept_order(self, client: Client):
        """
        Accepts order from client and makes Order object
        :param client: Client
        :return: Order / None
        """
        if client.make_order() is not None:
            wish, self.__tips = client.make_order()
            print(f'\nClient is ordering ...')
            order = Order(wish)
            print(f'Client ordered on ${order.amount}.')
            print(f'Waiter gained ${self.tips} tips.')
            return order
        return None

    @property
    def tips(self):
        """
        Property just to take tips of the certain waiter
        :return: float
        """
        return self.__tips


class Client:
    """
    Client class represents client itself
    """
    def __init__(self,
                 money: float,
                 client_name='Client1'):
        """
        Initializing client with certain number of money and name
        :param money: float
        :param client_name: str
        """
        self.name: str = client_name
        self.__money: float = money
        print(f'Client came to restaurant with ${money:.2f}.')

    def make_order(self):
        """
        Making order process and calculating general amount of the order
        :return: tuple (list of wishes-strings and float amount)
        """
        if self.__money < min(list(Order.menu.values())):
            return None
        wish = list()
        amount = self.__money + 1
        while self.__money < amount:
            wish = []
            price = 0
            for _ in range(randrange(1, 3)):
                dish = choice(list(Order.menu.keys()))
                wish.append(dish)
                price += Order.menu[dish]
            amount = price
        tips = self.__money
        while tips > self.__money - amount:
            tips = sum([randrange(0, 3) for _ in range(len(wish))])
        return wish, tips


class Restaurant:
    """
    Restaurant class represents general class in hierarchy
    """
    __daily_earnings = 0.
    __daily_tips = 0.

    def __init__(self, name, clients=5):
        """
        Initializing necessary attributes for restaurant working
        :param name: str
        :param clients: int
        """
        self.name: str = name
        if all([Cook.cooks.cook_equip['uniform'] == 4,
               Cook.cooks.cook_equip['kitchen-tools'] == 4]):
            self.chef = Chef()
            self.conf_c = Confectioner()
            self.meat_c = MeatCook()
            self.fish_c = FishCook()
            self.chef.set_next(self.conf_c).set_next(self.meat_c).set_next(self.fish_c)
            Cook.dishes = Cook.dishes
        elif all([Cook.cooks.cook_equip['uniform'] == 3,
                  Cook.cooks.cook_equip['kitchen-tools'] == 3]):
            self.chef = Chef()
            self.conf_c = Confectioner()
            self.meat_c = MeatCook()
            self.chef.set_next(self.conf_c).set_next(self.meat_c)
            del Cook.dishes['fish-cook']
            Order.menu = {key: Order.menu[key] for key in Order.menu.keys()
                          if key not in ('fish1', 'fish2', 'fish3')}
        if all([Waiter.waiters.waiter_equip['uniform'] == 2,
               Waiter.waiters.waiter_equip['waiter-tools'] == 2]):
            self.waiters = [Waiter() for i in range(2)]
        elif all([Waiter.waiters.waiter_equip['uniform'] == 1,
                  Waiter.waiters.waiter_equip['waiter-tools'] == 1]):
            self.waiters = [Waiter() for i in range(1)]
        self.clients = [Client(uniform(10., 140.4)) for i in range(clients)]

    def start_working(self):
        """
        Start restaurant working process (clients already came and waiter(s) have to accept them)
        :return: None
        """
        total_orders = []
        for client in self.clients:
            client.make_order()
            fastest_waiter = choice(self.waiters)
            total_orders.append(fastest_waiter.accept_order(client))
            self.__daily_tips += fastest_waiter.tips
            print(f'Total daily tips: {self.__daily_tips}')
        print('\n\nKitchen...')
        for order in total_orders:
            print(f'#{order.number}', order.dishes, order.amount)
            self.__daily_earnings += order.amount
            for dish in order.dishes:
                result = self.chef.cook(dish)
                print(result)
            print(f'#{order.number} is done!',
                  f'\nTotal daily earnings: {self.__daily_earnings}',
                  sep='', end='\n\n')


if __name__ == '__main__':
    my_restaurant = Restaurant('KhAI dining room', clients=6)
    my_restaurant.start_working()
