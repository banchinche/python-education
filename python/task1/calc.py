"""
This module contains Calculator that
realizes simple arithmetic operations
"""


class Calculator:
    """
    Calculator class, has such methods as

    - addition,
    - subtraction,
    - multiplying,
    - division
    """

    def __init__(self):
        """
        Initializing operands
        """
        self.first_operand: float = 0
        self.second_operand: float = 0

    def addition(self):
        """
        Takes static fields (first and second operands)
        :return: sum of two operands
        """
        return self.first_operand + self.second_operand

    def subtraction(self):
        """
        Takes static fields (first and second operands)
        :return: difference of two operands
        """
        return self.first_operand - self.second_operand

    def multiplying(self):
        """
        Takes static fields (first and second operands)
        :return: product of two operands
        """
        return self.first_operand * self.second_operand

    def division(self):
        """
        Takes static fields (first and second operands)
        :return: quotient of two operands
        """
        return self.first_operand / self.second_operand
