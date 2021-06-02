"""
Module to make several sessions of the game and calculating scores
"""
from game import TicTacToe
from menu import Menu
from player import Player, Human, Bot
from constants import LOGFILE, MESSAGE_FORMATTING, TIME_FORMAT
from typing import Union
import logging


logging.basicConfig(
     level=logging.INFO,
     filename=LOGFILE,
     format=MESSAGE_FORMATTING,
     datefmt=TIME_FORMAT)


class GameSession:
    """
    Game session class that provides several sessions of the game
    """
    def __init__(self) -> None:
        """
        Initializing score of the first player and second, menu instance
        """
        self.menu = Menu()
        self.game = None

    def start_session(self) -> None:
        """
        Starts session of the game
        :return: None
        """
        log = f'Session started...'
        logging.info(log)
        while True:
            choice = self.menu.show_menu()
            if choice == 4:
                break
            elif choice == 3:
                self.load_history()
            elif choice == 2:
                side1, side2 = TicTacToe.sides()
                player, bot = self.init_human_bot(side1, side2)
                self.start_game(player, bot)
            else:
                player1, player2 = self.init_humans()
                self.start_game(player1, player2)
        log = 'Exiting from the game...\n\n'
        logging.info(log)

    @staticmethod
    def congrats(player1: Player, player2: Player) -> None:
        """
        Congrats player (winner) and shows final battle result
        :param player1: Player
        :param player2: Player
        :return: None
        """
        if player1.score == player2.score:
            log = f'Result of the battle... Draw. {player1.name} vs {player2.name} with score ' \
                  f'{player1.score}:{player2.score}'
            print(log)
            logging.info(log)
        elif player1.score > player2.score:
            log = f'Result of the battle... Won {player1.name}! ' \
                  f'{player1.name} vs {player2.name} with score ' \
                  f'{player1.score}:{player2.score}'
            print(log)
            logging.info(log)
        elif player1.score < player2.score:
            log = f'Result of the battle... Won {player2.name}! ' \
                  f'{player1.name} vs {player2.name} with score ' \
                  f'{player1.score}:{player2.score}'
            print(log)
            logging.info(log)

    def start_game(self, player1: Human, player2: Union[Human, Bot]) -> None:
        """
        Chooses game mode (humans or human vs bot)
        :param player1: Player
        :param player2: Player
        :return: None
        """
        if isinstance(player2, Human):
            self.game = TicTacToe(player1=player1, player2=player2)
        else:
            self.game = TicTacToe(player1=player1, bot=player2)
        more = 'y'
        while more != 'n':
            more = self.game_loop(player1, player2)

    @staticmethod
    def update_scores(winner_side, player1, player2) -> None:
        """
        Updates scores and show them (prints and logs)
        :param winner_side: winner, str
        :param player1: Player
        :param player2: Player
        :return: None
        """
        if player1.player_side == winner_side:
            player1.score += 1
            print(f'{player1.name} as {player1.player_side} is won!')
        elif player2.player_side == winner_side:
            player2.score += 1
            print(f'{player2.name} as {player2.player_side} is won!')
        else:
            player1.score += 1
            player2.score += 1

    @staticmethod
    def init_humans() -> tuple:
        """
        Initializes two Human-players (fixed sides X-first)
        :return: tuple
        """
        player_name1 = input('Enter name for the first player: ')
        player1 = Human(player_name1, TicTacToe.X)
        player_name2 = input('Enter name for the second player: ')
        player2 = Human(player_name2, TicTacToe.O)
        return player1, player2

    @staticmethod
    def init_human_bot(side1: str, side2: str) -> tuple:
        """
        Initializes Human and Bot with given sides
        :param side1: str
        :param side2: str
        :return: tuple
        """
        player_name = input('Enter name for the player: ')
        player = Human(player_name, side1)
        bot = Bot(side2)
        return player, bot

    @staticmethod
    def load_history(filename='history.log'):
        """
        Prints history-file contents
        :param filename: str
        :return: None
        """
        with open(filename) as file:
            history = file.readlines()
            print(*history)
            logging.info('Browsing history of the sessions...')

    def game_loop(self, player1: Player, player2: Player) -> str:
        """
        Main game loop (game process of two players)
        :param player1: Player
        :param player2: Player
        :return: str
        """
        while not self.game.determine_winner():
            self.game.print_board()
            if self.game.current_turn == player1.player_side:
                self.game.make_move(player1)
            else:
                if isinstance(player2, Bot):
                    self.game.make_move(player=player2, cell=self.game.bot_move())
                else:
                    self.game.make_move(player=player2)
        winner = self.game.determine_winner()
        self.update_scores(winner, player1, player2)
        response = self.game.ask_for_more()
        if response == 'n':
            self.congrats(player1, player2)
            return 'n'
