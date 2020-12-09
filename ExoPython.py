from colorama import init
init()
from colorama import Fore, Back, Style
import random

finDuJeu = False
motsPossibles = ["suivre", "survie", "motard", "joyaux", "jockey", "aboyer", "angles", "animee", "canifs", "burger", "banane"]
indexMot = random.randint(0, len(motsPossibles) - 1)
motADeviner = motsPossibles[indexMot]
motPropose = ""


def compareMots(motPropose, motADeviner):
    print(motPropose, motADeviner)


while (finDuJeu == False):                                                                      #   DEBUT DE LA BOUCLE DE JEU


    while (len(motPropose) != 6):                                                               #
        motPropose = input("Quel mot proposez-vous de 6 caractères proposez-vous ?\n")          #   VERIFIE QUE LE MOT
        if (len(motPropose) != 6):                                                              #   CONTINENE BIEN 6 LETTRES
            print("Votre mot n'est pas composé de 6 caractères.")                               #
    
    print("Vous avez proposé le mot \"", motPropose , "\".\n")
    for i in range (0, 6):
        print(motPropose[i], end = " ")
    compareMots(motPropose, motADeviner)
        
        
    
    
    input()
    









print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
input()
