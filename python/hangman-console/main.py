"""
Script-runner that using to start playing
"""
from os import system, name as os_name
from string import ascii_letters
from hangman import Hangman
from random import choice, randrange


def start_game(game: Hangman):
    """
    Used as second menu (starting game after choosing 1 in main menu)
    :param game: Hangman class object to call methods
    :return:
    """
    first_char = input('Enter first char of a word: ')
    if len(first_char) != 1 or first_char == '':
        first_char = choice(ascii_letters[:len(ascii_letters) // 2])
    try:
        length = int(input('Enter length of a word: '))
    except ValueError:
        length = randrange(2, 10)
    except KeyError:
        length = 5
    if first_char in ascii_letters and length in range(2, 9):
        system('cls' if os_name == 'nt' else 'clear')
        game.generate_current_word(3, char=first_char, length=length)
    elif length in range(2, 9):
        system('cls' if os_name == 'nt' else 'clear')
        game.generate_current_word(2, length=length)
    elif first_char in ascii_letters:
        system('cls' if os_name == 'nt' else 'clear')
        game.generate_current_word(1, char=first_char)
    game.update_history_filename()
    entered = []
    while game.tries > 0:
        attempt = input('Enter full word or 1 symbol: ')
        entered.append(attempt)
        system('cls' if os_name == 'nt' else 'clear')
        if attempt == game.secret_word:
            print('Victory!')
            return
        game.attempt(attempt_str=attempt)
        game.show_current()
        if game.current_word == game.secret_word:
            print(f'Victory! The word was "{game.secret_word}"')
            return
        else:
            print('Your word:', game.show_current(), end='\n')
            print('You entered:', entered, end='\n')
            print('Tries remaining: ', game.tries, end='\n')
            print(game.display[5 - game.tries])

    else:
        print(f'You lost, the word was "{game.secret_word}". You hanged!', sep='\n')
    return


def menu():
    """
    Main menu of the program
    :return:
    """
    game = Hangman()
    print('1 - Start game!\n'
          '2 - Look previous words\n'
          '3 - Rules\n'
          '0 - Exit')
    try:
        menu_choice = int(input(': '))
    except ValueError:
        menu_choice = int(input(': '))
    if menu_choice == 1:
        start_game(game=game)
    elif menu_choice == 2:
        print(''.join(game.load_previous_words()))
    elif menu_choice == 3:
        print('https://en.wikipedia.org/wiki/Hangman_(game)')
    elif menu_choice == 0:
        return 0


if __name__ == '__main__':
    system('cls' if os_name == 'nt' else 'clear')
    tmp = 1
    while tmp != 0:
        tmp = menu()
        if tmp != 0:
            input('\nPress Enter to continue...')
            system('cls' if os_name == 'nt' else 'clear')
