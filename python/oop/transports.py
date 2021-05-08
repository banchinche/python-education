"""
Transport classes inherited from the base 'Transport'
"""
from abc import ABC, abstractmethod
from random import choice


class Transport(ABC):
    """
    Base transport class
    """
    _number_of_wheels = 0
    _possible_brands = tuple()

    def __init__(self,
                 *args):
        """
        Initializing instance of the class

        :param args: Arguments that will be parsed
        """
        self.speed: float = float()
        self.weight: float = float()
        self.color: str = str()
        self.parse_arguments(*args)

    @property
    def p_color(self):
        """
        Color getter
        :return:
        """
        return self.color

    @p_color.setter
    def p_color(self, color: str):
        self.color = color

    @p_color.deleter
    def p_color(self):
        self.color = 'no color'

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @abstractmethod
    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """

    @classmethod
    def get_wheels(cls):
        """
        Getting static class attribute that shows number of wheels
        :return:
        """
        return cls._number_of_wheels

    @classmethod
    def get_brand(cls):
        """
        Getting static class attribute that shows brand
        :return:
        """
        return cls._possible_brands


class Engine:
    """
    Engine base class
    """
    _possible_category = ('Inline',
                          'V-type',
                          'Boxer',
                          'W-type')

    def __init__(self, *args):
        """
        Initializing instance of the engine

        :param args: Arguments that will be parsed
        :return:
        """
        self.power: float = float()
        self.torque: float = float()
        self.category = choice(self.get_category())
        self.parse_arguments(*args)

    def __str__(self):
        """
        Shows all attributes of the engine

        :return:
        """
        return 'Engine has such characteristics:\n' + f'- power: {self.power}\n' + \
               f'- torque: {self.torque}\n' + f'- category: {self.category}\n'

    @classmethod
    def get_category(cls):
        """
        Getting static class attribute that shows category of engine
        :return:
        """
        return cls._possible_category

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """
        assert len(args) == 2
        self.power = args[0]
        self.torque = args[1]


class Bicycle(Transport):
    """
    Bicycle transport inheritor
    """
    _number_of_wheels = 2
    _possible_brands = ('TopRider',
                        'Apollo',
                        'Cyclone',
                        'Discovery',
                        'Formula')

    def __init__(self, *args):
        """
        Initializing instance of the bicycle

        :param speed: float, shows speed of the bicycle
        :param weight: float, shows weight of the bicycle
        :param color: str, color of the bicycle
        :param brand: str, brand of the bicycle
        """
        super().__init__(*args)
        if self.brand not in self._possible_brands:
            self.brand = choice(self._possible_brands)

    def __str__(self):
        """
        Shows all attributes of the bicycle instance

        :return:
        """
        return 'Bicycle\n' + f'Speed: {self.speed} km/h\n' + \
               f'Weight: {self.weight} kilos\n' + f'Color: {self.color}\n' + \
               f'Brand: {self.brand}\n'

    def __call__(self, *args, **kwargs):
        """
        Changes float values of the instance calling that one

        :param args: new values to change
        :param kwargs:
        :return:
        """
        self.speed, self.weight = args[0], args[1]

    def __eq__(self, other):
        """
        Equality check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed == other.speed,
                    self.weight == other.weight,
                    self.color == other.color,
                    self.brand == other.brand])

    def __ne__(self, other):
        """
        Inequality check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed != other.speed,
                    self.weight != other.weight,
                    self.color != other.color,
                    self.brand != other.brand])

    def __lt__(self, other):
        """
        Less than check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: {"less" if self.speed < other.speed else "greater"}',
                f' - weight: {"less" if self.weight < other.weight else "greater"}']

    def __le__(self, other):
        """
        Less or equal check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less or equal" if self.speed <= other.speed else "greater or equal"}',
                f' - weight: '
                f'{"less or equal" if self.weight <= other.weight else "greater or equal"}']

    def __gt__(self, other):
        """
        Greater than check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: {"greater" if self.speed > other.speed else "less"}',
                f' - weight: {"greater" if self.weight > other.weight else "less"}']

    def __ge__(self, other):
        """
        Greater or equal check

        :param other: another instance of the Bicycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater or equal" if self.speed >= other.speed else "less or equal"}',
                f' - weight: '
                f'{"greater or equal" if self.weight >= other.weight else "less or equal"}']

    @classmethod
    def get_brand(cls):
        """
        Getting static class attribute that shows brand
        :return:
        """
        return cls._possible_brands

    def parse_arguments(self, *args):
        assert len(args) == 4
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]
        self.brand = args[3]


class Motorcycle(Bicycle, Engine):
    """
    Motorcycle bicycle and Engine inheritor
    """
    _number_of_wheels = 2
    _possible_brands = ('BMW',
                        'Honda',
                        'Kawasaki',
                        'Suzuki')

    def __str__(self):
        """
        Shows all attributes of the motorcycle instance

        :return:
        """
        engine_chars = Engine.__str__(self)
        return 'Motorcycle\n' + f'Speed: {self.speed} km/h\n' + \
               f'Weight: {self.weight} kilos\n' + f'Color: {self.color}\n' + \
               f'Brand: {self.brand}\n' + engine_chars

    def __call__(self, *args, **kwargs):
        """
        Changes float values of the instance calling that one

        :param args: new values to change
        :param kwargs:
        :return:
        """
        self.speed = args[0]
        self.weight = args[1]
        self.power = args[2]
        self.torque = args[3]

    def __eq__(self, other):
        """
        Equality check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed == other.speed,
                    self.weight == other.weight,
                    self.color == other.color,
                    self.brand == other.brand,
                    self.power == other.power,
                    self.torque == other.torque])

    def __ne__(self, other):
        """
        Inequality check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed != other.speed,
                    self.weight != other.weight,
                    self.color != other.color,
                    self.brand != other.brand,
                    self.power != other.power,
                    self.torque != other.torque])

    def __lt__(self, other):
        """
        Less than check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less" if self.speed < other.speed else "greater"}',
                f' - weight: '
                f'{"less" if self.weight < other.weight else "greater"}',
                f' - power: '
                f'{"less" if self.power < other.power else "greater"}',
                f' - torque: '
                f'{"less" if self.torque < other.torque else "greater"}'
                ]

    def __le__(self, other):
        """
        Less or equal check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less or equal" if self.speed <= other.speed else "greater or equal"}',
                f' - weight: '
                f'{"less or equal" if self.weight <=other.weight else "greater or equal"}',
                f' - power: '
                f'{"less or equal" if self.power <= other.power else "greater or equal"}',
                f' - torque: '
                f'{"less or equal" if self.torque <= other.torque else "greater or equal"}'
                ]

    def __gt__(self, other):
        """
        Greater than check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater" if self.speed > other.speed else "less"}',
                f' - weight: '
                f'{"greater" if self.weight > other.weight else "less"}',
                f' - power: '
                f'{"greater" if self.power > other.power else "less"}',
                f' - torque: '
                f'{"greater" if self.torque > other.torque else "less"}'
                ]

    def __ge__(self, other):
        """
        Greater or equal check

        :param other: another instance of the Motorcycle
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater or equal" if self.speed >= other.speed else "less or equal"}',
                f' - weight: '
                f'{"greater or equal" if self.weight >= other.weight else "less or equal"}',
                f' - power: '
                f'{"greater or equal" if self.power >= other.power else "less or equal"}',
                f' - torque: '
                f'{"greater or equal" if self.torque >= other.torque else "less or equal"}'
                ]

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """
        assert len(args) == 6
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]
        self.brand = args[3]
        self.power = args[4]
        self.torque = args[5]
        self.category = choice(self.get_category())


class Car(Transport, Engine):
    """
    Car transport inheritor
    """
    _number_of_wheels = 4
    _possible_brands = ('Alfa Romeo',
                        'Hyundai',
                        'Reno',
                        'Opel',
                        'Mercedes')

    def __init__(self, *args):
        """
        Initializing instance of the car

        :param speed: float, shows speed of the car
        :param weight: float, shows weight of the car
        :param color: str, color of the car
        :param brand: str, brand of the car
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        """
        super().__init__(*args)
        if self.brand not in self._possible_brands:
            self.brand = choice(self.get_brand())

    def __str__(self):
        """
        Shows all attributes of the car instance

        :return:
        """
        engine_chars = Engine.__str__(self)
        return 'Car\n' + f'Speed: {self.speed} km/h\n' + \
               f'Weight: {self.weight} kilos\n' + f'Color: {self.color}\n' + \
               f'Brand: {self.brand}\n' + engine_chars

    def __call__(self, *args, **kwargs):
        """
        Changes float values of the instance calling that one

        :param args: new values to change
        :param kwargs:
        :return:
        """
        self.speed = args[0]
        self.weight = args[1]
        self.power = args[2]
        self.torque = args[3]

    def __eq__(self, other):
        """
        Equality check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed == other.speed,
                    self.weight == other.weight,
                    self.color == other.color,
                    self.brand == other.brand,
                    self.power == other.power,
                    self.torque == other.torque])

    def __ne__(self, other):
        """
        Inequality check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed != other.speed,
                    self.weight != other.weight,
                    self.color != other.color,
                    self.brand != other.brand,
                    self.power != other.power,
                    self.torque != other.torque])

    def __lt__(self, other):
        """
        Less than check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less" if self.speed < other.speed else "greater"}',
                f' - weight: '
                f'{"less" if self.weight < other.weight else "greater"}',
                f' - power: '
                f'{"less" if self.power < other.power else "greater"}',
                f' - torque: '
                f'{"less" if self.torque < other.torque else "greater"}'
                ]

    def __le__(self, other):
        """
        Less or equal check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less or equal" if self.speed <= other.speed else "greater or equal"}',
                f' - weight: '
                f'{"less or equal" if self.weight <=other.weight else "greater or equal"}',
                f' - power: '
                f'{"less or equal" if self.power <= other.power else "greater or equal"}',
                f' - torque: '
                f'{"less or equal" if self.torque <= other.torque else "greater or equal"}'
                ]

    def __gt__(self, other):
        """
        Greater than check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater" if self.speed > other.speed else "less"}',
                f' - weight: '
                f'{"greater" if self.weight > other.weight else "less"}',
                f' - power: '
                f'{"greater" if self.power > other.power else "less"}',
                f' - torque: '
                f'{"greater" if self.torque > other.torque else "less"}'
                ]

    def __ge__(self, other):
        """
        Greater or equal check

        :param other: another instance of the Car
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater or equal" if self.speed >= other.speed else "less or equal"}',
                f' - weight: '
                f'{"greater or equal" if self.weight >= other.weight else "less or equal"}',
                f' - power: '
                f'{"greater or equal" if self.power >= other.power else "less or equal"}',
                f' - torque: '
                f'{"greater or equal" if self.torque >= other.torque else "less or equal"}'
                ]

    @classmethod
    def get_brand(cls):
        """
        Getting static class attribute that shows brand
        :return:
        """
        return cls._possible_brands

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """
        assert len(args) == 6
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]
        self.brand = args[3]
        self.power = args[4]
        self.torque = args[5]
        self.category = choice(self._possible_category)


class Plane(Transport, Engine):
    """
    Plane transport inheritor
    """
    _number_of_wheels = choice([3, 4, 16, 18])
    _number_of_wings = choice([2, 4])
    _possible_brands = ('Airbus',
                        'Boeing',
                        'Lockheed Martin',
                        'Northrop Grumman',
                        'Rolls-Royce Holdings')

    def __init__(self, *args):
        """
        Initializing instance of the plane

        :param speed: float, shows speed of the plane
        :param weight: float, shows weight of the plane
        :param color: str, color of the plane
        :param brand: str, brand of the plane
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        """

        super().__init__(*args)
        if self.brand not in self._possible_brands:
            self.brand = choice(self.get_brand())

    def __str__(self):
        """
        Shows all attributes of the plane instance

        :return:
        """
        engine_chars = Engine.__str__(self)
        return 'Plane\n' + f'Speed: {self.speed} km/h\n' + \
               f'Weight: {self.weight} kilos\n' + f'Color: {self.color}\n' + \
               f'Brand: {self.brand}\n' + f'Count of aircraft wings: {self.get_wings()}\n' + \
               engine_chars

    def __call__(self, *args, **kwargs):
        """
        Changes float values of the instance calling that one

        :param args: new values to change
        :param kwargs:
        :return:
        """
        self.speed = args[0]
        self.weight = args[1]
        self.power = args[2]
        self.torque = args[3]

    def __eq__(self, other):
        """
        Equality check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed == other.speed,
                    self.weight == other.weight,
                    self.color == other.color,
                    self.brand == other.brand,
                    self.power == other.power,
                    self.torque == other.torque])

    def __ne__(self, other):
        """
        Inequality check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all([self.speed != other.speed,
                    self.weight != other.weight,
                    self.color != other.color,
                    self.brand != other.brand,
                    self.power != other.power,
                    self.torque != other.torque])

    def __lt__(self, other):
        """
        Less than check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less" if self.speed < other.speed else "greater"}',
                f' - weight: '
                f'{"less" if self.weight < other.weight else "greater"}',
                f' - power: '
                f'{"less" if self.power < other.power else "greater"}',
                f' - torque: '
                f'{"less" if self.torque < other.torque else "greater"}'
                ]

    def __le__(self, other):
        """
        Less or equal check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"less or equal" if self.speed <= other.speed else "greater or equal"}',
                f' - weight: '
                f'{"less or equal" if self.weight <=other.weight else "greater or equal"}',
                f' - power: '
                f'{"less or equal" if self.power <= other.power else "greater or equal"}',
                f' - torque: '
                f'{"less or equal" if self.torque <= other.torque else "greater or equal"}'
                ]

    def __gt__(self, other):
        """
        Greater than check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater" if self.speed > other.speed else "less"}',
                f' - weight: '
                f'{"greater" if self.weight > other.weight else "less"}',
                f' - power: '
                f'{"greater" if self.power > other.power else "less"}',
                f' - torque: '
                f'{"greater" if self.torque > other.torque else "less"}'
                ]

    def __ge__(self, other):
        """
        Greater or equal check

        :param other: another instance of the Plane
        :return:
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return [f' - speed: '
                f'{"greater or equal" if self.speed >= other.speed else "less or equal"}',
                f' - weight: '
                f'{"greater or equal" if self.weight >= other.weight else "lessor equal"}',
                f' - power: '
                f'{"greater or equal" if self.power >= other.power else "less or equal"}',
                f' - torque: '
                f'{"greater or equal" if self.torque >= other.torque else "less or equal"}'
                ]

    @classmethod
    def get_brand(cls):
        """
        Getting static class attribute that shows brand
        :return:
        """
        return cls._possible_brands

    @classmethod
    def get_wings(cls):
        """
        Getting static class attribute that shows number of wings
        :return:
        """
        return cls._number_of_wings

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """
        assert len(args) == 6
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]
        self.brand = args[3]
        self.power = args[4]
        self.torque = args[5]
        self.category = choice(self.get_category())


class JetSki(Motorcycle):
    """
    Jet ski  transport and motorcycle inheritor
    """
    _number_of_wheels = Transport.get_wheels()
    _possible_brands = Motorcycle.get_brand()

    def __str__(self):
        """
        Shows all attributes of the jet ski instance

        :return:
        """
        engine_chars = Engine.__str__(self)
        return 'Jet ski\n' + f'Speed: {self.speed} km/h\n' + \
               f'Weight: {self.weight} kilos\n' + f'Color: {self.color}\n' + \
               f'Brand: {self.brand}\n' + engine_chars

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments

        :param args:
        :return:
        """
        assert len(args) == 6
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]
        self.brand = args[3]
        self.power = args[4]
        self.torque = args[5]
        self.category = choice(self.get_category())


if __name__ == '__main__':
    # something1 = Transport(45, 23.5, 'red')
    # print(something1)
    something2 = Bicycle(20, 15.7, 'blue', 'asap')
    print(something2)
    something3 = Motorcycle(320, 82.5, 'black', 'seqweqw', 120.5, 150.2)
    print(something3)
    # print(Motorcycle.__mro__)
    something4 = Car(290, 24.13584e3, 'white', 'seqweqw', 120.5, 150.2)
    print(something4)
    something5 = Plane(600, 7.21451e3, 'azure', 'sasdkFJAJF', 120.5, 150.2)
    print(something5)
    something6 = JetSki(320, 72.5, 'yellow', 'sewqeqwe', 120.5, 150.2)
    print(something6)
    # print(JetSki.__mro__)

    # Property task
    print('Property checking in the JetSki Transport-inheritor:', something6.p_color)
    # Changing color
    something6.p_color = 'another color'
    print('Changed to another color:', something6.p_color)
    del something6.p_color
    print('Deleted color:', something6.p_color)

    # Showing magic methods in Bicycle, inheritor of the abstract Transport
    first_bicycle = Bicycle(45, 23.5, 'red', 'TopRider')
    second_bicycle = Bicycle(45, 23.5, 'red', 'TopRider')
    print('\nEquality of two instances:', first_bicycle == second_bicycle)

    first_bicycle(22, 20)
    print('\nLess than another:', *(first_bicycle < second_bicycle), sep='\n')
    print('\nLess or equal to another:', *(first_bicycle <= second_bicycle), sep='\n')

    print('\nAnother greater than first:', *(second_bicycle > first_bicycle), sep='\n')
    print('\nAnother greater or equal to first:', *(second_bicycle >= first_bicycle), sep='\n')

    # And the example of the overloaded magic methods in the Car Transport-inheritor
    first_car = Car(290, 24.13e3, 'white', 'Reno', 120.5, 150.2)
    second_car = Car(290, 24.13e3, 'white', 'Reno', 120.5, 150.2)
    print('\nEquality of two instances:', first_car == second_car)

    first_car(22, 20, 22, 20)

    print('\nLess than another:', *(first_car < second_car), sep='\n')
    print('\nLess or equal to another:', *(first_car <= second_car), sep='\n')

    print('\nAnother greater than first:', *(second_car > first_car), sep='\n')
    print('\nAnother greater or equal to first:', *(second_car >= first_car), sep='\n')
