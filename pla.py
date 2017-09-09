from os import system
from colorama import Fore, init
from pyfiglet import Figlet


PLANETS = {
    '': '',
}

QUESTIONS = [
    ('Atmosphere', 'Yes', 'No'),
    ('Water', 'Yes', 'No'),
    ('Number of moons', '0', '1', '2', '3', '4'),
    ('Surface', 'Cotofotelum', 'Vistulum', 'Pulcherium', 'Triodecennium'),
]


init(autoreset=True)
F = Figlet()
DONE = False

while not DONE:
    system('clear')
    print(Fore.GREEN + F.renderText('Planet\nDatabase'))
    answers = []
    for item in QUESTIONS:
        question, *options = item
        available_answers = ', '.join(
            '{}: {}'.format(i, t) for i, t in enumerate(options)
        )
        print('{} [{}]:'.format(question, available_answers))
        while True:
            answer = input()
            if answer.isdigit() and int(answer) < len(options):
                break
            print(Fore.RED + 'Incorrect option')
        answers.append(str(answer))
    key = ''.join(answers)
    planet = PLANETS.get(key, 'UNKNOWN')
    print('The planet is:')
    print(Fore.YELLOW + planet)
    print('Press Enter to search again')
    input()
