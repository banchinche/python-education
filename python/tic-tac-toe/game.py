"""
Here is the main logic of the game
"""
from player import Player, Human, Bot
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

    def __init__(self, player1: Human = None, player2: Human = None, bot: Bot = None) -> None:
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
        self.bot = bot

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
        """
        Computes all possible moves based on EMPTY mark or not
        :return: None
        """
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
                return winner

    @staticmethod
    def make_choice(player) -> int:
        """
        Choosing number of the cell
        :return: int
        """
        response = None
        while response not in range(9):
            try:
                response = int(input(f'{player.name}\'s turn now ({player.player_side}).\n'
                                     f'Enter cell number (0-8): '))
            except ValueError:
                pass
        return response

    def make_move(self, player: Player, cell=None) -> None:
        """
        Makes move on the board as given player
        :return: None
        """
        self.possible_moves()
        if cell is None:
            move = None
            while move not in self.possible:
                move = self.make_choice(player)
                if move not in self.possible:
                    print('\nThat square is already occupied. Choose another.\n')
            self.board[move] = player.player_side
        else:
            self.board[cell] = player.player_side
        self.next_turn()

    def next_turn(self) -> None:
        """
        Makes a transition to the next turn
        :return: None
        """
        if self.current_turn == self.X:
            self.current_turn = self.O
        else:
            self.current_turn = self.X

    def bot_move(self) -> int:
        """
        Makes bot move (return index on the board)
        :return: int
        """
        best_score = -10
        self.possible_moves()
        for cell in self.possible:
            self.board[cell] = self.bot.side
            score = self.minimax(False)
            self.board[cell] = self.EMPTY
            if score > best_score:
                best_score = score
                best_move = cell
        return best_move

    def minimax(self, maximize: bool) -> int:
        """
        Returns integer score of certain move
        :param maximize: boolean parameter for recursive call
        :return: int
        """
        if self.determine_winner() == self.bot.side:
            return 10
        elif self.determine_winner() == self.first_player.side:
            return -10
        elif self.determine_winner() == self.TIE:
            return 0
        self.possible_moves()
        if maximize:
            best_score = -10
            for cell in self.possible:
                self.board[cell] = self.bot.side
                score = self.minimax(False)
                self.board[cell] = self.EMPTY
                if score > best_score:
                    best_score = score
            return best_score
        else:
            best_score = 10
            for cell in self.possible:
                self.board[cell] = self.first_player.side
                score = self.minimax(True)
                self.board[cell] = self.EMPTY
                if score < best_score:
                    best_score = score
            return best_score

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

    @staticmethod
    def sides() -> tuple:
        """
        Based on choice, returns sides of players
        :return: tuple of strings
        """
        player_side = input('Enter player\'s side(X / O): ').upper()
        return player_side, TicTacToe.X if player_side == TicTacToe.O else TicTacToe.O
