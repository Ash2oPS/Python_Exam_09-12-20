from colorama import init
init()
from colorama import Fore, Back, Style
import random

finDuJeu = False
nombreDeVies = 8
motsPossibles = ["suivre", "survie", "motard", "joyaux", "jockey", "aboyer", "angles", "animee", "canifs", "burger", "banane", "jouets", "castor", "marbre", "kinder", "ecrans", "donjon", "mouche", "mousse", "pigeon", "unreal", "amours", "souris", "chauve", "ongles", "cheveu", "suites", "steaks", "taupes", "marche", "devins", "pauvre", "riches", "sucres"]
indexMot = random.randint(0, len(motsPossibles) - 1)
motADeviner = motsPossibles[indexMot]
motPropose = ""

'''
def boucleIndexLettresCorrectes(lettre, indexLettresCorrectes):
    output = False

    for j in range (0, len(indexLettresCorrectes)):
        if (indexLettresCorrectes[j] == lettre):
            output = True
    return output


def afficherCouleurs(motPropose, indexLettresCorrectes):
    for i in range (0, len(motPropose)):
        print(boucleIndexLettresCorrectes(motPropose[i], indexLettresCorrectes))
        if (boucleIndexLettresCorrectes(motPropose[i], indexLettresCorrectes) == True):
            #print(Back.YELLOW, motPropose[i], Style.RESET_ALL, end = "")
        else:
            print(motPropose[i])
'''
        

    
    


def compareMots(motPropose, motADeviner):

    lettreComparee = ""
    lettresCorrectes = ""
    indexLettresCorrectes = ""
    
    print("(Mot proposé :", motPropose, ". Mot à deviner :", motADeviner, ". Cette ligne sera supprimée quand le programme fonctionnera.)") #POUR DEBUG
    for i in range (0, len(motPropose)):                                                    #
        lettreComparee = motPropose[i].lower()                                              #JE VOULAIS FAIRE EN SORTE
        for j in range (0, len(motADeviner)):                                               #QU'ELLE PERMETTE D'OBTENIR
            if lettreComparee == motADeviner[j]:                                            #LES LETTRES CORRECTES ET
                lettresCorrectes += lettreComparee                                          #LEUR INDICE
                indexLettresCorrectes += str(i)                                             #
                
    #print(lettresCorrectes, indexLettresCorrectes)
    #afficherCouleurs(motPropose, indexLettresCorrectes)

            


while (finDuJeu == False)  and (nombreDeVies != 0):                                         #DEBUT DE LA BOUCLE DE JEU                                        

    motPropose = ""
    while (len(motPropose) != 6):                                                           #
        print("Tentatives restantes :", nombreDeVies, ".")                                  #VERIFIE QUE LE 
        motPropose = input("Quel mot de 6 caractères proposez-vous ?\n")                    #MOT CONTIENNE
        if (len(motPropose) != 6):                                                          #BIEN 6 CARACTERES
            print("Votre mot n'est pas composé de 6 caractères.")                           #   
    
    nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne = 0                                  #VERIFIE SI CHAQUE
    for i in range (0, len(motPropose)):                                                    #LETTRE DU MOT PROPOSE
        if (motADeviner[i].lower() == motPropose[i].lower()):                               #EST BIEN EGALE A LA LETTRE
            nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne += 1                         #PARTAGEANT LE MEME INDEX CHEZ
    if nombreDeLettresCorrectesPourSavoirSiLeJoueurAGagne == 6:                             #LE MOT A DEVINER
            finDuJeu = True                                                                 #SI OUI, LE JOUEUR A GAGNE
            
    nombreDeVies -= 1
    print("Vous avez proposé le mot \"", motPropose , "\".\n")
    '''for i in range (0, len(motPropose)):
        print(motPropose[i], end = " ")'''
    print("\n")
    compareMots(motPropose, motADeviner)
        
                                                                                            #FIN DE LA BOUCLE DE JEU
                                                                                            #SI LE JOUEUR A 0 VIE, C'EST
                                                                                            #QU'IL A PERDU, SINON IL
                                                                                            #A GAGNE
    
if (nombreDeVies == 0):
    print("Vous avez perdu. Vous ferez mieux la prochaine fois ! (comme moi d'ailleurs, puisque mon programme ne marche pas.)")
else:
    print("Yes ! Bien joué, vous avez gagné !")
input()
    


