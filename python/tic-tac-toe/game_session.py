"""
Module to make several sessions of the game and calculating scores
"""
from game import TicTacToe
from menu import Menu
from player import Player
from constants import LOGFILE, MESSAGE_FORMATTING, TIME_FORMAT
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
    def __init__(self):
        """
        Initializing score of the first player and second, menu instance
        """
        self.first_score = 0
        self.second_score = 0
        self.menu = Menu()

    def start_session(self) -> None:
        """
        Starts session of the game
        :return: None
        """
        log = f'Session started...'
        logging.info(log)
        while True:
            choice = self.menu.show_menu()
            if choice == 3:
                break
            elif choice == 2:
                self.load_history()
            else:
                more_than_one = None
                player_name1 = input('Enter name for the first player: ')
                player1 = Player(player_name1, TicTacToe.X)
                player_name2 = input('Enter name for the second player: ')
                player2 = Player(player_name2, TicTacToe.O)
                self.game = TicTacToe(player1, player2)
                while not self.game.determine_winner():
                    self.game.print_board()
                    if self.game.current_turn == player1.side:
                        move = self.game.make_move()
                        self.game.board[move] = player1.side
                    else:
                        move = self.game.make_move()
                        self.game.board[move] = player2.side
                winner = self.game.determine_winner()
                more_than_one = self.game.ask_for_more()
                if more_than_one == 'y':
                    if winner == self.game.X:
                        self.first_score += 1
                    elif winner == self.game.O:
                        self.second_score += 1
                    else:
                        self.first_score += 1
                        self.second_score += 1
                    print(f'Take revenge! Current status '
                          f'{self.first_score}:{self.second_score}')
                    while more_than_one != 'n':
                        self.game = TicTacToe(player1, player2)
                        while not self.game.determine_winner():
                            self.game.print_board()
                            if self.game.current_turn == player1.side:
                                move = self.game.make_move()
                                self.game.board[move] = player1.side
                            else:
                                move = self.game.make_move()
                                self.game.board[move] = player2.side
                        winner = self.game.determine_winner()
                        if player1.side == winner:
                            self.first_score += 1
                        elif player2.side == winner:
                            self.second_score += 1
                        else:
                            self.first_score += 1
                            self.second_score += 1
                        print(f'{self.first_score}:{self.second_score}')
                        battle_continue = self.game.ask_for_more()
                        if battle_continue == 'n':
                            log = f'{player1.name} vs {player2.name} result is ' \
                                  f'{self.first_score}:{self.second_score}'
                            logging.info(log)
                            more_than_one = 'n'
                else:
                    if player1.side == winner:
                        self.congrats(player1)
                        print(f'{player1.name} is won!')
                    elif player2.side == winner:
                        self.congrats(player2)
                        print(f'{player2.name} is won!')
                    else:
                        self.congrats(self.game.TIE)
            self.first_score = 0
            self.second_score = 0
        log = 'Exiting from the game...\n\n'
        logging.info(log)

    @staticmethod
    def congrats(player=None) -> None:
        """
        Checks for the winner and prints him (if it's one-game mode)
        :param player: Player
        :return: None
        """
        if player == TicTacToe.TIE:
            log = 'Draw.'
            print(log)
            logging.info(log)
        else:
            log = f'Won {player.name} with {player.side} side!'
            print(log)
            logging.info(log)

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
