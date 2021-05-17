"""
Main function
"""
from game_session import GameSession


def main() -> None:
    """
    Just starts the game
    :return:
    """
    g = GameSession()
    g.start_session()


if __name__ == '__main__':
    main()
