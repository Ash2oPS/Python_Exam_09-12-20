from colorama import init
init()
from colorama import Fore, Back, Style
import random

motsPossibles = ["suivre", "survie", "motard", "joyaux", "jockey", "aboyer", "angles", "animee", "canifs", "burger"]
indexMot = random.randint(0, 9)
motADeviner = motsPossibles[indexMot]












print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
input()
