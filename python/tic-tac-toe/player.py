"""
Helpful player-class module
"""
from abc import ABC


class Player(ABC):
    def __init__(self, name: str, side: str):
        """
        Initializes name and side of the player
        :param name: str
        :param side: str
        """
        self.name = name
        self.side = side
        self.score = 0

    @property
    def player_side(self) -> str:
        return self.side

    @player_side.setter
    def player_side(self, side: str) -> None:
        self.side = side


class Human(Player):
    """
    Helps with operating names and sides (X or O)
    """
    def __init__(self, name: str, side: str):
        super().__init__(name, side)


class Bot(Player):
    def __init__(self, side: str):
        super().__init__('Computer', side)
