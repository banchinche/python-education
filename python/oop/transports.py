"""
Transport classes inherited from the base 'Transport'
"""
from random import choice


class Transport:
    """
    Base transport class
    """
    _number_of_wheels = 0

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str):
        """
        Initializing instance of the class
        :param speed: float, shows speed of the transport
        :param weight: float, shows weight of the transport
        :param color: str, color of the transport
        """
        self.speed: float = speed
        self.weight: float = weight
        self.color: str = color

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


class Engine:
    """
    Engine base class
    """
    possible_category = ('Inline',
                         'V-type',
                         'Boxer',
                         'W-type')

    def __init(self, power: float,
               torque: float,
               consumption: float):
        """
        Initializing instance of the engine
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        :param consumption: float, shows specific fuel consumption of the engine
        :return:
        """
        self.power: float = power
        self.torque: float = torque
        self.spec_fuel_consumption: float = consumption
        self.category = choice(self.possible_category)

    def show_info(self):
        """
        Shows all attributes of the engine
        :return:
        """
        print('Engine has such characteristics:',
              f'- power: {self.power}',
              f'- torque: {self.torque}',
              f'- specific fuel consumption: {self.spec_fuel_consumption}',
              f'- category: {self.category}',
              sep='\n')


class Bicycle(Transport):
    """
    Bicycle transport inheritor
    """
    _number_of_wheels = 2
    possible_brands = ('TopRider',
                       'Apollo',
                       'Cyclone',
                       'Discovery',
                       'Formula')

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str):
        """
        Initializing instance of the bicycle
        :param speed: float, shows speed of the bicycle
        :param weight: float, shows weight of the bicycle
        :param color: str, color of the bicycle
        :param brand: str, brand of the bicycle
        """
        super().__init__(speed, weight, color)
        self.brand: str
        if brand in self.possible_brands:
            self.brand = brand
        else:
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


class Motorcycle(Bicycle, Engine):
    """
    Motorcycle bicycle and Engine inheritor
    """
    _number_of_wheels = 2
    possible_brands = ('BMW',
                       'Harley-Davidson',
                       'Honda',
                       'Kawasaki',
                       'Suzuki')

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 power: float,
                 torque: float,
                 consumption: float):
        """
        Initializing instance of the motorcycle
        :param speed: float, shows speed of the motorcycle
        :param weight: float, shows weight of the motorcycle
        :param color: str, color of the motorcycle
        :param brand: str, brand of the motorcycle
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        :param consumption: float, shows specific fuel consumption of the engine
        """
        super().__init__(speed, weight, color, brand)
        self.power = power
        self.torque = torque
        self.spec_fuel_consumption = consumption
        self.category = choice(Engine.possible_category)

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


class Car(Transport, Engine):
    """
    Car transport inheritor
    """
    _number_of_wheels = 4
    possible_brands = ('Alfa Romeo',
                       'Hyundai',
                       'Reno',
                       'Opel',
                       'Mercedes')

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 power: float,
                 torque: float,
                 consumption: float):
        """
        Initializing instance of the car
        :param speed: float, shows speed of the car
        :param weight: float, shows weight of the car
        :param color: str, color of the car
        :param brand: str, brand of the car
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        :param consumption: float, shows specific fuel consumption of the engine
        """
        super().__init__(speed, weight, color)
        if brand in self.possible_brands:
            self.brand = brand
        else:
            self.brand = choice(self.possible_brands)
        self.power = power
        self.torque = torque
        self.spec_fuel_consumption = consumption
        self.category = choice(Engine.possible_category)

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


class Plane(Transport, Engine):
    """
    Plane transport inheritor
    """
    _number_of_wheels = choice([3, 4, 16, 18])
    _number_of_wings = choice([2, 4])
    possible_brands = ('Airbus',
                       'Boeing',
                       'Lockheed Martin',
                       'Northrop Grumman',
                       'Rolls-Royce Holdings')

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 power: float,
                 torque: float,
                 consumption: float):
        """
        Initializing instance of the plane
        :param speed: float, shows speed of the plane
        :param weight: float, shows weight of the plane
        :param color: str, color of the plane
        :param brand: str, brand of the plane
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        :param consumption: float, shows specific fuel consumption of the engine
        """
        super().__init__(speed, weight, color)
        if brand in self.possible_brands:
            self.brand = brand
        else:
            self.brand = choice(self.possible_brands)
        self.power = power
        self.torque = torque
        self.spec_fuel_consumption = consumption
        self.category = choice(Engine.possible_category)

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
              f'Count of aircraft wings: {self._number_of_wings}',
              sep='\n')
        Engine.show_info(self)


class JetSki(Motorcycle):
    """
    Jet ski  transport and motorcycle inheritor
    """
    number_of_wheels = Transport._number_of_wheels
    possible_brands = Motorcycle.possible_brands

    def __init__(self, speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 power: float,
                 torque: float,
                 consumption: float):
        """
        Initializing instance of the jet ski
        :param speed: float, shows speed of the jet ski
        :param weight: float, shows weight of the jet ski
        :param color: str, color of the jet ski
        :param brand: str, brand of the jet ski
        :param power: float, shows power of the engine
        :param torque: float, shows torque of the engine
        :param consumption: float, shows specific fuel consumption of the engine
        """
        super().__init__(speed, weight, color, brand, power, torque, consumption)

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


if __name__ == '__main__':
    something1 = Transport(45, 23.5, 'red')
    something1.show_info()
    print()
    something2 = Bicycle(20, 15.7, 'blue', 'adspf')
    something2.show_info()
    print()
    something3 = Motorcycle(320, 82.5, 'black', 'seqweqw', 120.5, 150.2, 102.5)
    something3.show_info()
    print()
    print(Motorcycle.__mro__)
    something4 = Car(290, 24.13584e3, 'white', 'seqweqw', 120.5, 150.2, 102.5)
    something4.show_info()
    print()
    something5 = Plane(600, 7.21451e3, 'azure', 'sasdkFJAJF', 120.5, 150.2, 102.5)
    something5.show_info()
    print()
    something6 = JetSki(320, 72.5, 'yellow', 'sewqeqwe', 120.5, 150.2, 102.5)
    something6.show_info()
    print(JetSki.__mro__)
