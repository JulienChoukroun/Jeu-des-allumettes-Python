#Choukroun-Mittaine

#jeu des allumettes
#version de base
#règles: le joueur joue contre l'ordinateur. un nombre aléatoire d'allumette-tortues est affiché.
#        Le joueur commence.
#        A chaque tour, le joueur enlève 1,2 ou 3 allumette-tortues. Puis l'ordinateur joue.
#        Le gagnant est celui qui prend la dernière allumette.

import random

#definition des fonctions

def tourJoueurEtOrdi(totalAllumettes,allumetteARetirer) :
    nbAllumettes=totalAllumettes-allumetteARetirer #le nombre d'allumette est recalculé en fonction de l'entier entré par le joueur et par l'ordi
    if nbAllumettes<0 : #si le nombre d'allumettes restante est inférieur à 0, on met la valeur à 0
        nbAllumettes=0
    return nbAllumettes

def lancementJeu(totalAllumettes) :
    gagnant=False
    while gagnant==False :
        #le joueur joue
        allumetteJoueur=int(input("Combien d'allumettes voulez-vous retirer (entre 1 et 3) ? "))
        if allumetteJoueur<1 or allumetteJoueur>3 : #le joueur peut retirer uniquement entre 1 et 3 allumettes
            print("Vous ne pouvez retirer que 1,2 ou 3 d'allumettes")
        else :
            totalAllumettes=tourJoueurEtOrdi(totalAllumettes,allumetteJoueur)
            print("Le nombre d'allumettes restantes est",totalAllumettes) #on affiche le nombre d'allumettes restantes
            if totalAllumettes==0 :
                gagnant=True
                nomGagnant="joueur"
            else :
                #l'ordinateur joue
                allumetteOrdi=random.randint(1,3) #c'est au tour de l'ordinateur, il prend au hasard entre 1 et 3 allumettes
                print("L'ordinateur retire",allumetteOrdi,"allumettes") #on montre au joueur ce que l'ordinateur a enlevé au nombre total
                totalAllumettes=tourJoueurEtOrdi(totalAllumettes,allumetteOrdi)
                print("Le nombre d'allumettes restantes est",totalAllumettes) #on affiche le nombre d'allumettes restantes
                if totalAllumettes==0 :
                    gagnant=True
                    nomGagnant="ordinateur"
    return nomGagnant
    
#fin définitions des fonctions

#programme principal

totalAllumettes=random.randint(10,20)
#l'ordinateur choisi un nombre aléatoire d'allumettes entre 10 et 20

print("Le nombre d'allumette est :",totalAllumettes)
#on affiche les allumettes

#le jeu continue tant qu'il n'y a pas de gagnant
nomGagnant=lancementJeu(totalAllumettes)

#on affiche le nom du gagnant
print("Le gagnant est : ",nomGagnant)

#fin du programme
