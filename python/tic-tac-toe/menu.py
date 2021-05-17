"""
Menu module stores string menu template
"""


class Menu:
    """
    Menu class just prints menu
    """
    def __init__(self):
        pass

    @staticmethod
    def show_menu() -> int:
        """
        Selecting one choice from given (main menu)
        :return: int
        """
        print("""
Welcome to the Tic-tac-toe console game!
Follow such rules, pick one of the unused cell, according to this board:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8

1 - start game (2 humans)
2 - history of the games
3 - quit
        """)
        while True:
            try:
                choice = int(input('Enter value from menu: '))
                if choice not in [1, 2, 3]:
                    raise ValueError
            except ValueError:
                continue
            return choice
