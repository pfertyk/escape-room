from os import system
from colorama import Fore, init
from pyfiglet import Figlet


PLANETS = {
    '0000': '',
    '0001': '',
    '0002': '',
    '0003': '',
    '0010': '',
    '0011': '',
    '0012': '',
    '0013': '',
    '0020': '',
    '0021': '',
    '0022': '',
    '0023': '',
    '0030': '',
    '0031': '',
    '0032': '',
    '0033': '',
    '0040': '',
    '0041': '',
    '0042': '',
    '0043': '',
    '0100': '',
    '0101': '',
    '0102': '',
    '0103': '',
    '0110': '',
    '0111': '',
    '0112': '',
    '0113': '',
    '0120': '',
    '0121': '',
    '0122': '',
    '0123': '',
    '0130': '',
    '0131': '',
    '0132': '',
    '0133': '',
    '0140': '',
    '0141': '',
    '0142': 'Lestretis',
    '0143': 'Oscadus',
    '1000': 'Badrion',
    '1001': 'Griri',
    '1002': 'Xiaphus',
    '1003': 'Theneos',
    '1010': 'Aprouhiri',
    '1011': 'Botadus',
    '1012': 'Opryke',
    '1013': 'Soyrus',
    '1020': 'Yecury',
    '1021': 'Yiaruta',
    '1022': 'Gehorth',
    '1023': 'Stosamia',
    '1030': 'Kiovis',
    '1031': 'Skagua',
    '1032': 'Meuris',
    '1033': 'Cusceus',
    '1040': 'Cillion',
    '1041': 'Tuglilia',
    '1042': 'Aenope',
    '1043': 'Daclides',
    '1100': 'Gubos',
    '1101': 'Zuspara',
    '1102': 'Resteyn',
    '1103': 'Ustruna',
    '1110': 'Sceron',
    '1111': 'Pruolia',
    '1112': 'Mosmyria',
    '1113': 'Greron',
    '1120': 'Iaeter',
    '1121': 'Teaturn',
    '1122': 'Geonides',  # the one
    '1123': 'Cruna',
    '1130': 'Scorix',
    '1131': 'Spart',
    '1132': 'Kearus',
    '1133': 'Oglade',
    '1140': 'Glides',
    '1141': 'Draqua',
    '1142': 'Beolea',
    '1143': 'Fenope',
}

QUESTIONS = [
    ('Atmosphere', 'No', 'Yes'),
    ('Water', 'No', 'Yes'),
    ('Number of moons', '0', '1', '2', '3', '4'),
    ('Surface', 'Vistulum', 'Pulcherium', 'Cotofotelum', 'Triodecennium'),
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
