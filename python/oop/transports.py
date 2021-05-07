"""
Transport classes inherited from the base 'Transport'
"""
from random import choice


class Transport:
    """
    Base transport class
    """
    number_of_wheels = 0

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

    def show_info(self):
        """
        Shows all attributes of the transport instance
        :return:
        """
        print('Transport',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              sep='\n')

    def parse_arguments(self, *args):
        """
        Parsing arguments to avoid pylint mistakes with too much arguments
        :param args:
        :return:
        """
        assert len(args) == 3
        self.speed = args[0]
        self.weight = args[1]
        self.color = args[2]


class Engine:
    """
    Engine base class
    """
    possible_category = ('Inline',
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
        self.category = choice(self.possible_category)
        self.parse_arguments(*args)

    def show_info(self):
        """
        Shows all attributes of the engine
        :return:
        """
        print('Engine has such characteristics:',
              f'- power: {self.power}',
              f'- torque: {self.torque}',
              f'- category: {self.category}',
              sep='\n')

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
    number_of_wheels = 2
    possible_brands = ('TopRider',
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
        if self.brand not in self.possible_brands:
            self.brand = choice(self.possible_brands)

    def show_info(self):
        """
        Shows all attributes of the bicycle instance
        :return:
        """
        print('Bicycle',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              f'Brand: {self.brand}',
              sep='\n')

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
    number_of_wheels = 2
    possible_brands = ('BMW',
                       'Honda',
                       'Kawasaki',
                       'Suzuki')

    def show_info(self):
        """
        Shows all attributes of the motorcycle instance
        :return:
        """
        print('Motorcycle',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              f'Brand: {self.brand}',
              sep='\n')
        Engine.show_info(self)

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
        self.category = choice(self.possible_category)


class Car(Transport, Engine):
    """
    Car transport inheritor
    """
    number_of_wheels = 4
    possible_brands = ('Alfa Romeo',
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
        if self.brand not in self.possible_brands:
            self.brand = choice(self.possible_brands)

    def show_info(self):
        """
        Shows all attributes of the car instance
        :return:
        """
        print('Car',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              f'Brand: {self.brand}',
              sep='\n')
        Engine.show_info(self)

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
        self.category = choice(self.possible_category)


class Plane(Transport, Engine):
    """
    Plane transport inheritor
    """
    number_of_wheels = choice([3, 4, 16, 18])
    number_of_wings = choice([2, 4])
    possible_brands = ('Airbus',
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
        if self.brand not in self.possible_brands:
            self.brand = choice(self.possible_brands)

    def show_info(self):
        """
        Shows all attributes of the plane instance
        :return:
        """
        print('Plane',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              f'Brand: {self.brand}',
              f'Count of aircraft wings: {self.number_of_wings}',
              sep='\n')
        Engine.show_info(self)

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
        self.category = choice(self.possible_category)


class JetSki(Motorcycle):
    """
    Jet ski  transport and motorcycle inheritor
    """
    number_of_wheels = Transport.number_of_wheels
    possible_brands = Motorcycle.possible_brands

    def show_info(self):
        """
        Shows all attributes of the jet ski instance
        :return:
        """
        print('Jet ski',
              f'Speed: {self.speed} km/h',
              f'Weight: {self.weight} kilos',
              f'Color: {self.color}',
              f'Brand: {self.brand}',
              sep='\n')
        Engine.show_info(self)

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
        self.category = choice(self.possible_category)


if __name__ == '__main__':
    something1 = Transport(45, 23.5, 'red')
    something1.show_info()
    print()
    something2 = Bicycle(20, 15.7, 'blue', 'asap')
    something2.show_info()
    print()
    something3 = Motorcycle(320, 82.5, 'black', 'seqweqw', 120.5, 150.2)
    something3.show_info()
    print()
    # print(Motorcycle.__mro__)
    something4 = Car(290, 24.13584e3, 'white', 'seqweqw', 120.5, 150.2)
    something4.show_info()
    print()
    something5 = Plane(600, 7.21451e3, 'azure', 'sasdkFJAJF', 120.5, 150.2)
    something5.show_info()
    print()
    something6 = JetSki(320, 72.5, 'yellow', 'sewqeqwe', 120.5, 150.2)
    something6.show_info()
    # print(JetSki.__mro__)
