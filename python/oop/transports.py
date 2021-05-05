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


class Bicycle(Transport):
    """
    Bicycle transport inheritor
    """
    number_of_wheels = 2
    possible_brands = ['TopRider',
                       'Apollo',
                       'Cyclone',
                       'Discovery',
                       'Formula']

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


class Motorcycle(Bicycle):
    """
    Motorcycle bicycle inheritor
    """
    number_of_wheels = 2
    possible_brands = ['BMW',
                       'Harley-Davidson',
                       'Honda',
                       'Kawasaki',
                       'Suzuki']

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 motor_power: float):
        """
        Initializing instance of the motorcycle
        :param speed: float, shows speed of the motorcycle
        :param weight: float, shows weight of the motorcycle
        :param color: str, color of the motorcycle
        :param brand: str, brand of the motorcycle
        :param motor_power: float, shows power of the motorcycle motor
        """
        super().__init__(speed, weight, color, brand)
        self.motor_power = motor_power

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
              f'Motor power: {self.motor_power}',
              sep='\n')


class Car(Transport):
    """
    Car transport inheritor
    """
    number_of_wheels = 4
    possible_brands = ['Alfa Romeo',
                       'Hyundai',
                       'Reno',
                       'Opel',
                       'Mercedes']

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 motor_power: float):
        """
        Initializing instance of the car
        :param speed: float, shows speed of the car
        :param weight: float, shows weight of the car
        :param color: str, color of the car
        :param brand: str, brand of the car
        :param motor_power: float, shows power of the car motor
        """
        super().__init__(speed, weight, color)
        if brand in self.possible_brands:
            self.brand = brand
        else:
            self.brand = choice(self.possible_brands)
        self.motor_power: float = motor_power

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
              f'Motor power: {self.motor_power}',
              sep='\n')


class Plane(Transport):
    """
    Plane transport inheritor
    """
    number_of_wheels = choice([3, 4, 16, 18])
    number_of_wings = choice([2, 4])
    possible_brands = ['Airbus',
                       'Boeing',
                       'Lockheed Martin',
                       'Northrop Grumman',
                       'Rolls-Royce Holdings']

    def __init__(self,
                 speed: float,
                 weight: float,
                 color: str,
                 brand: str,
                 motor_power: float):
        """
        Initializing instance of the plane
        :param speed: float, shows speed of the plane
        :param weight: float, shows weight of the plane
        :param color: str, color of the plane
        :param brand: str, brand of the plane
        :param motor_power: float, shows power of the plane motor
        """
        super().__init__(speed, weight, color)
        if brand in self.possible_brands:
            self.brand = brand
        else:
            self.brand = choice(self.possible_brands)
        self.motor_power: float = motor_power

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
              f'Motor power: {self.motor_power}',
              f'Count of aircraft wings: {self.number_of_wings}',
              sep='\n')


if __name__ == '__main__':
    something1 = Transport(45, 23.5, 'red')
    something1.show_info()
    print()
    something2 = Bicycle(20, 15.7, 'blue', 'adspf')
    something2.show_info()
    print()
    something3 = Motorcycle(320, 82.5, 'black', 'seqweqw', 98.7)
    something3.show_info()
    print()
    something4 = Car(290, 24.13584e3, 'white', 'seqweqw', 98.7)
    something4.show_info()
    print()
    something5 = Plane(600, 7.21451e3, 'azure', 'sasdkFJAJF', 98.7)
    something5.show_info()
