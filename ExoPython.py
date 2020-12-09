from colorama import init
init()
from colorama import Fore, Back, Style
import random

finDuJeu = False
nombreDeVies = 8
motsPossibles = ["suivre", "survie", "motard", "joyaux", "jockey", "aboyer", "angles", "animee", "canifs", "burger", "banane", "jouets", "castor", "marbre", "kinder", "ecrans", "donjon"]
indexMot = random.randint(0, len(motsPossibles) - 1)
motADeviner = motsPossibles[indexMot]
motPropose = ""

def boucleIndexLettresCorrectes(lettre, indexLettresCorrectes):
    output = False

    for j in range (0, len(indexLettresCorrectes)):
        if (indexLettresCorrectes[j] == lettre):
            output = True
    return output


#def afficherCouleurs(motPropose, indexLettresCorrectes):
    #for i in range (0, len(motPropose)):
        #print(boucleIndexLettresCorrectes(motPropose[i], indexLettresCorrectes))
        #if (boucleIndexLettresCorrectes(motPropose[i], indexLettresCorrectes) == True):
            #print(Back.YELLOW, motPropose[i], Style.RESET_ALL, end = "")
        #else:
            #print(motPropose[i])
        
        

    
    


def compareMots(motPropose, motADeviner):

    lettreComparee = ""
    lettresCorrectes = ""
    indexLettresCorrectes = ""
    
    print("(", motPropose, motADeviner, ")")
    for i in range (0, len(motPropose)):
        lettreComparee = motPropose[i].lower()
        for j in range (0, len(motADeviner)):
            if lettreComparee == motADeviner[j]:
                lettresCorrectes += lettreComparee
                indexLettresCorrectes += str(i)
                
    print(lettresCorrectes, indexLettresCorrectes)
    #afficherCouleurs(motPropose, indexLettresCorrectes)

            


while (finDuJeu == False)  and (nombreDeVies != 0):                                                                     

    motPropose = ""
    while (len(motPropose) != 6):                                   
        print("Tentatives restantes :", nombreDeVies, ".")
        motPropose = input("Quel mot de 6 caractères proposez-vous ?\n")         
        if (len(motPropose) != 6):                                                            
            print("Votre mot n'est pas composé de 6 caractères.")                               
    
    nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne = 0
    for i in range (0, len(motPropose)):
        if (motADeviner[i] == motPropose[i]):
            nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne += 1
    if nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne == 6:
            finDuJeu == True
    nombreDeVies -= 1
    print("Vous avez proposé le mot \"", motPropose , "\".\n")
    '''for i in range (0, len(motPropose)):
        print(motPropose[i], end = " ")'''
    print("\n")
    compareMots(motPropose, motADeviner)
        
        
    
if (nombreDeVies == 0):
    print("Vous avez perdu. Vous ferez mieux la prochaine fois ! (comme moi d'ailleurs, puisque mon programme ne marche pas.)")
else:
    print("Yes ! Bien joué, vous avez gagné !")
input()
    


