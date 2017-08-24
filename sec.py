from os import system
from random import choice, sample
from time import sleep

from pyfiglet import Figlet
from termcolor import colored

PASSWORDS = {
    'yellow': {
        'ABC': '1456',
        'ABD': '1457',
    },
    'red': {
        'BBC': '2456',
        'BBD': '2457',
    },
    'blue': {
        'CBC': '3456',
        'CBD': '3457',
    },
    'cyan': {
        'DBC': '4456',
        'DBD': '4457',
    },
    'green': {
        'EBC': '5456',
        'EBD': '5457',
    },
    'magenta': {
        'FBC': '6456',
        'FBD': '6457',
    },
}


f = Figlet()
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
    print(colored(f.renderText('Security System'), 'yellow', attrs=['bold']))

    passwords = set()

    for color, key, _ in expected_passwords:
        print(colored('  ' + key + '  ', 'grey', 'on_' + color), end='')
        password = input(': ')
        passwords.add((color, key, password))

    if passwords == expected_passwords:
        print(colored(f.renderText('OK 4536'), 'green'))
        done = True
    else:
        print(colored(f.renderText('ERROR'), 'red'), end='')
        sleep(3)


while True:
    pass
