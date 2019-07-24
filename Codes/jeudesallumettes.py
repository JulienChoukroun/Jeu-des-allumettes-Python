#Choukroun-Mittaine

#jeu des tortues-allumettes
#version de base
#règles: Le joueur joue contre l'ordinateur. Un nombre aléatoire de tortues-allumettes est affiché.
#        Le joueur commence.
#        A chaque tour, le joueur enlève 1,2 ou 3 tortue(s)-allumette(s). Puis l'ordinateur joue.
#        Le gagnant est celui qui prend la dernière tortue-allumette.

#on importe les modules
import random
from turtle import*
from time import*
from petitetortue import*
from decor_final import*


#definition des fonctions

#la fonction tourJoueurEtOrdi calcule le nombre de tortues-allumettes restantes
#retourne ce nombre
def tourJoueurEtOrdi(totalAllumettes,allumetteARetirer) :
    nbAllumettes=int(totalAllumettes-allumetteARetirer) #le nombre de tortues-allumettes est recalculé en fonction de l'entier entré par le joueur et par l'ordinateur
    if nbAllumettes<0 : #si le nombre de tortues-allumettes restante est inférieur à 0, on met la valeur à 0
        nbAllumettes=0
    return nbAllumettes

#la fonction lancementJeu fait jouer le joueur et l'ordinateur à tour de rôle jusqu'à ce qu'il n'y ait plus de tortues-allumettes
#retourne le nom du gagnant (joueur ou ordinateur)
def lancementJeu(totalAllumettes) :
    gagnant=False
    while gagnant==False :
        #le joueur joue
        allumetteJoueur=numinput("Joueur","Combien de tortues-allumettes voulez-vous retirer (entre 1 et 3) ? ",1,1,3) #le joueur choisi entre 1 et 3 tortue(s)-allumette(s)
        totalAllumettes=tourJoueurEtOrdi(totalAllumettes,allumetteJoueur) #le nombre de tortues-allumettes est recalculé
        clear() #on efface l'affichage de l'écran
        setheading(0) #on remet les paramètres d'orientation par défault
        dessineDecor() #on redessine le décor
        affichageAllumettes(totalAllumettes) #on affiche les tortues-allumettes restantes
        strTotalAllumettes=str(totalAllumettes)
        if totalAllumettes>1 : #permet de mettre un "s" à la fin du mot "tortue-allumette"
            texteAllumettesRestantes="Il y a "+strTotalAllumettes+" tortues-allumettes"
        else :
            texteAllumettesRestantes="Il y a "+strTotalAllumettes+" tortue-allumette"
        up()
        goto(0,-150)
        down()
        color("black")
        write(texteAllumettesRestantes,align="center",font=("Arial",24,"normal")) #on écrit le nombre de tortues-allumettes restantes
        sleep(3) #on fait une pause dans le temps de 3 secondes
        undo() #on supprime cette dernière action
        if totalAllumettes==0 :
            gagnant=True
            nomGagnant="Vous avez gagné !"
        else :
            #l'ordinateur joue
            up()
            goto(0,-150)
            down()
            write("L'ordinateur joue",align="center",font=("Arial",24,"normal"))
            sleep(2) #on fait une pause dans le temps de 2 secondes
            allumetteOrdi=random.randint(1,3) #c'est au tour de l'ordinateur, il prend au hasard entre 1 et 3 tortue(s)-allumette(s)
            strAllumettesOrdi=str(allumetteOrdi)
            if allumetteOrdi>1 : #permet de mettre un "s" à la fin du mot "tortue-allumette"
                texteAllumettesOrdi="L'ordinateur a retiré "+strAllumettesOrdi+" tortues-allumettes"
            else :
                texteAllumettesOrdi="L'ordinateur a retiré "+strAllumettesOrdi+" tortue-allumette"
            totalAllumettes=tourJoueurEtOrdi(totalAllumettes,allumetteOrdi) #le nombre de tortues-allumettes est recalculé
            strTotalAllumettes=str(totalAllumettes)
            clear() #on efface l'affichage de l'écran
            setheading(0) #on remet les paramètres d'orientation par défault
            dessineDecor() #on redessine le décor
            affichageAllumettes(totalAllumettes) #on affiche les tortues-allumettes restantes
            up()
            goto(0,-100)
            down()
            color("black")
            write(texteAllumettesOrdi,align="center",font=("Arial",24,"normal")) #on écrit le nombre de tortues-allumettes que l'ordinateur a retiré
            if totalAllumettes>1 : #permet de mettre un "s" à la fin du mot "tortue-allumette"
                texteAllumettesRestantes="Il y a "+strTotalAllumettes+" tortues-allumettes"
            else :
                texteAllumettesRestantes="Il y a "+strTotalAllumettes+" tortue-allumette"
            up()
            goto(0,-150)
            down()
            color("black")
            write(texteAllumettesRestantes,align="center",font=("Arial",24,"normal")) #on écrit le nombre de tortues-allumettes restantes
            sleep(3) #on fait une pause dans le temps de 3 secondes
            if totalAllumettes==0 :
                gagnant=True
                nomGagnant="L'ordinateur a gagné !"
                
    return nomGagnant #la fonction retourne le nom du gagnant

#la procédure affichageAllumettes dessine les tortues-allumettes selon le nombre de tortues-allumettes choisi par le joueur et l'ordinateur
def affichageAllumettes(totalAllumettes) :
    speed(0)
    tracer(0)
    x=(-window_width())/2 +100 #on se place a gauche de la fenêtre pour commencer à dessiner
    up()
    goto(x,0)
    down()
    i=0
    while i<totalAllumettes : #tant que toutes les tortues-allumettes ne sont pas dessinées, on applique cette boucle, c'est-à-dire, on dessine une nouvelle tortue-allumette
        setheading(0) #on remet les paramètres d'orientation par défault
        dessineTortue(x) #dessine une tortue-allumette. Cette procédure se trouve dans le fichier petitetortue.py
        up()
        x=x+100
        goto(x,0)
        down()
        i=i+1
    up()
    
#fin définition des fonctions


#programme principal

title("Jeu des tortues-allumettes")

totalAllumettes=random.randint(11,17) #l'ordinateur choisi un nombre aléatoire de tortues-allumettes entre 11 et 17
largeur=totalAllumettes*110
setup(largeur,800) #on défini la taille de la fenêtre
hideturtle() #rend la tortue invisible

#initialisation de la fenêtre de jeu et du décor
#appel aux fonctions et procédures de decor_final.py
dessineDecor() #on dessine le décor. Cette procédure se trouve dans le fichier decor_final.py

affichageAllumettes(totalAllumettes) #on affiche les tortues-allumettes

strTotalAllumettes=str(totalAllumettes)
texteTotalAllumettes="Il y a "+strTotalAllumettes+" tortues-allumettes"
up()
goto(0,-150)
down()
color("black")
write(texteTotalAllumettes,align="center",font=("Arial",24,"normal")) #on écrit le nombre total de tortues-allumettes

#le jeu continue tant qu'il n'y a pas de gagnant
nomGagnant=lancementJeu(totalAllumettes)

#on affiche le nom du gagnant
up()
goto(0,0)
down()
color("black")
write(nomGagnant,align="center",font=("Arial",30,"normal"))

#fin du programme
