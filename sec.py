from os import system
from random import choice, sample
from time import sleep

from colorama import Back, Fore, Style, init
from pyfiglet import Figlet

PASSWORDS = {
    'green': {
        'PWXGAB': '048251',
        'CTZQYK': '072158',
        'BQRGWL': '670145',
        'PUZGCY': '724130',
        'VAPUEK': '152703',
        'WIQNKP': '162495',
        'ECXQFR': '912374',
        'MXSLEZ': '943725',
        'UIVMPH': '387914',
        'GOTCRD': '693180'
    },
    'magenta': {
        'SVUDJG': '153047',
        'TDVOMX': '493157',
        'JMNYSC': '250476',
        'UZYITH': '849607',
        'TJDFCR': '172380',
        'ETQJUO': '106584',
        'COTUJP': '459610',
        'IXOMFK': '163804',
        'SPIAHV': '561294',
        'QMOFIH': '023918'
    },
    'cyan': {
        'XQFWES': '193082',
        'PHWMQS': '261948',
        'LGRYCZ': '816492',
        'FVTKZJ': '752861',
        'SQTXRO': '917256',
        'YFLQEB': '579432',
        'EXNGBU': '329547',
        'ETGUOP': '613289',
        'KTHNJE': '263975',
        'GZYDVS': '049875'
    },
    'blue': {
        'OJPKNE': '053714',
        'MGCDTE': '682075',
        'TDESXW': '617039',
        'CLMTNQ': '457312',
        'VGUINM': '796341',
        'YRHVLS': '527481',
        'SOAYQH': '678530',
        'TLBUYO': '973218',
        'HNIAOR': '219645',
        'DNSAXK': '068753'
    },
    'yellow': {
        'HUFMVN': '253071',
        'VNUCPS': '643702',
        'GCEJOH': '127439',
        'QKXRTP': '487132',
        'PUKLHD': '716982',
        'QMXUAV': '704123',
        'XIMFUK': '142705',
        'JUYHOD': '198630',
        'SOPYZA': '649025',
        'TJMLYA': '962145'
    },
    'red': {
        'DULQZV': '534917',
        'KHJUWO': '809342',
        'QZVKCI': '739052',
        'WHLJOX': '364128',
        'NGDRQC': '365270',
        'HWJUND': '304825',
        'QEFNTG': '407285',
        'RKLAZT': '419678',
        'VGHUJX': '154978',
        'JIDYVU': '402568'
    }
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
        print()
        passwords.add((color, key, password))

    return passwords


def print_header():
    system('clear')
    print(Fore.YELLOW + Style.BRIGHT + F.renderText('Security System'))


def print_access_code():
    print(Style.BRIGHT + Fore.GREEN + F.renderText('>>  987  <<'))


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
