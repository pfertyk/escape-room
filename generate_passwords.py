from json import dumps
from random import sample


colors = {'red', 'yellow', 'green', 'blue', 'cyan', 'magenta'}
digits = '0123456789'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


passwords = {}

for color in colors:
    passwords[color] = {}
    while len(passwords[color].keys()) < 10:
        code = ''.join(sample(letters, 6))
        value = ''.join(sample(digits, 6))

        passwords[color][code] = value

print(dumps(passwords, indent=4))
