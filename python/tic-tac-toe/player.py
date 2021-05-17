"""
Helpful player-class module
"""


class Player:
    """
    Helps with operating names and sides (X or O)
    """

    def __init__(self, name: str, side: str):
        """
        Initializes name and side of the player
        :param name: str
        :param side: str
        """
        self.name = name
        self.side = side
