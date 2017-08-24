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


f = Figlet()
init(autoreset=True)
done = False

while not done:
    all_colors = set(PASSWORDS.keys())
    all_colors.remove('yellow')

    colors = {'yellow'}
    colors.update(sample(all_colors, 3))

    expected_passwords = set()

    for color in colors:
        key = choice(list(PASSWORDS[color].keys()))
        correct_pass = PASSWORDS[color][key]
        expected_passwords.add((color, key, correct_pass))

    system('clear')
    print(Fore.YELLOW + Style.BRIGHT + f.renderText('Security System'))

    passwords = set()

    for color, key, _ in expected_passwords:
        back_color = getattr(Back, color.upper())
        print(Style.BRIGHT + back_color + '  ' + key + '  ', end='')
        password = input(': ')
        passwords.add((color, key, password))

    if passwords == expected_passwords:
        print(Fore.GREEN + f.renderText('>>  4536  <<'))
        done = True
    else:
        print(Fore.RED + f.renderText('ERROR'))
        sleep(3)


while True:
    pass
