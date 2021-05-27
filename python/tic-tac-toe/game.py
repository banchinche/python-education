"""
Here is the main logic of the game
"""
from player import Player
from typing import Union
from constants import EMPTY_MARK, X_MARK, O_MARK, TIE_MARK


class TicTacToe:
    """
    Game class
    """
    EMPTY = EMPTY_MARK
    X = X_MARK
    O = O_MARK
    TIE = TIE_MARK
    BOARD_SIZE = 9
    WIN_CONDITION = ((0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 8),
                     (2, 4, 6))

    def __init__(self, player1: Player, player2: Player):
        """
        Initializing players and board
        :param player1: Player
        :param player2: Player
        """
        self.board = list()
        for cell in range(self.BOARD_SIZE):
            self.board.append(self.EMPTY)
        self.possible = list()
        self.current_turn = self.X
        self.first_player = player1
        self.second_player = player2

    def print_board(self) -> None:
        """
        Just prints current board view
        :return:
        """
        cell = self.board
        print(f'   Current board\t Hint-board')
        print(f'\t {cell[0]} | {cell[1]} | {cell[2]} \t\t 0 | 1 | 2')
        print(f'\t-----------\t\t------------')
        print(f'\t {cell[3]} | {cell[4]} | {cell[5]} \t\t 3 | 4 | 5')
        print(f'\t-----------\t\t------------')
        print(f'\t {cell[6]} | {cell[7]} | {cell[8]} \t\t 6 | 7 | 8')

    def possible_moves(self) -> None:
        possible = list()
        for cell in range(self.BOARD_SIZE):
            if self.board[cell] == self.EMPTY:
                possible.append(cell)
        self.possible = possible

    def determine_winner(self) -> str:
        """
        Check if there any winner or tie
        :return: str
        """
        if self.EMPTY not in self.board:
            return self.TIE
        for win in self.WIN_CONDITION:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]] != self.EMPTY:
                winner = self.board[win[0]]
                print(f'{winner} is winner!')
                return winner

    @staticmethod
    def make_choice() -> int:
        """
        Choosing number of the cell
        :return: int
        """
        response = None
        while response not in range(9):
            try:
                response = int(input('Enter cell number (0-8): '))
            except ValueError:
                pass
        return response

    def make_move(self) -> int:
        """
        Check if cell is already occupied and return its number
        :return: int
        """
        self.possible_moves()
        move = None
        while move not in self.possible:
            move = self.make_choice()
            if move not in self.possible:
                print('\nThat square is already occupied. Choose another.\n')
        self.next_turn()
        return move

    def next_turn(self) -> None:
        """
        Makes a transition to the next turn
        :return: None
        """
        if self.current_turn == self.X:
            self.current_turn = self.O
        else:
            self.current_turn = self.X

    @staticmethod
    def ask_for_more() -> str:
        """
        Asks for more games in one battle with the same players
        :return: str
        """
        response = None
        while response not in ('y', 'n'):
            response = input('Would you like to play more as these players?\n: ').lower()
        return response
