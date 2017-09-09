import textwrap
from os import system
from colorama import Fore, init


def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string


MESSAGE = '''
This is a message
There is a table here:
Jupiter     | 12345
Saturn      | 34643
'''
password_matches = False
password = 'space'

init(autoreset=True)
system('clear')

while not password_matches:
    print(textwrap.fill(encode(password, MESSAGE), 20))
    print(Fore.RED + '='*20)
    print(Fore.RED + 'Access denied')
    if input('password: ') == password:
        password_matches = True
    system('clear')

print(Fore.GREEN + 'Access granted')
print(Fore.GREEN + '='*20)
print(MESSAGE)

while True:
    input()
