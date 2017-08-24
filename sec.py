from os import system
from random import choice, sample
from time import sleep

from colorama import Back, Fore, Style, init
from pyfiglet import Figlet

PASSWORDS = {
    'yellow': {
        'ABC': '1234',
        'ABD': '1234',
    },
    'red': {
        'BBC': '1234',
        'BBD': '1234',
    },
    'blue': {
        'CBC': '1234',
        'CBD': '1234',
    },
    'cyan': {
        'DBC': '1234',
        'DBD': '1234',
    },
    'green': {
        'EBC': '1234',
        'EBD': '1234',
    },
    'magenta': {
        'FBC': '1234',
        'FBD': '1234',
    },
}

init(autoreset=True)
F = Figlet()
DONE = False


def select_random_passwords(passwords):
    all_colors = set(passwords.keys())
    all_colors.remove('yellow')

    colors = {'yellow'}
    colors.update(sample(all_colors, 3))

    random_passwords = set()

    for color in colors:
        key = choice(list(passwords[color].keys()))
        correct_password = passwords[color][key]
        random_passwords.add((color, key, correct_password))

    return random_passwords


def get_passwords_from_user(expected_passwords):
    passwords = set()

    for color, key, _ in expected_passwords:
        back_color = getattr(Back, color.upper())
        print(Style.BRIGHT + back_color + '  ' + key + '  ', end='')
        password = input(': ')
        passwords.add((color, key, password))

    return passwords


def print_header():
    system('clear')
    print(Fore.YELLOW + Style.BRIGHT + F.renderText('Security System'))


def print_access_code():
    print(Style.BRIGHT + Fore.GREEN + F.renderText('>>  4536  <<'))


def print_error_message():
    clear_line = '\r\033[K\033[F'
    for i in range(4):
        print(Style.BRIGHT + Fore.RED + F.renderText('ERROR'), end='')
        sleep(0.3)
        print(clear_line * 7)
        sleep(0.3)


while not DONE:
    print_header()

    expected_passwords = select_random_passwords(PASSWORDS)
    passwords = get_passwords_from_user(expected_passwords)

    if passwords == expected_passwords:
        print_access_code()
        DONE = True
    else:
        print_error_message()


while True:
    pass
