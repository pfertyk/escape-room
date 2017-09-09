from os import system
from colorama import Fore, init
from pyfiglet import Figlet


PLANETS = {
    '': '',
}

QUESTIONS = [
    ('Atmosphere', 'Yes', 'No'),
    ('Number of moons', '0', '1', '2', '3', '4'),
    ('Main element', 'Element1', 'Element2', 'Element3'),
    ('Water', 'Yes', 'No'),
]


init(autoreset=True)
F = Figlet()
DONE = False

while not DONE:
    system('clear')
    print(Fore.Green + F.renderText('Planet Database'))
    answers = []
    for item in QUESTIONS:
        question, *options = item
        ans = ', '.join('{}: {}'.format(i, t) for i, t in enumerate(options))
        print('{} [{}]:'.format(question, ans))
        while True:
            answer = input()
            if answer.isdigit() and int(answer) < len(options):
                break
            print(Fore.RED + 'Incorrect option')
        answers.append(str(answer))
    key = ''.join(answers)
    planet = PLANETS.get(key, 'UNKNOWN')
    print('The planet is: ' + planet)
    print('Press Enter to search again')
    input()
