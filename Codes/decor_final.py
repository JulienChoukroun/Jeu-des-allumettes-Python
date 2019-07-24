#Choukroun-Mittaine

from turtle import *
import random

#dessine les vagues : cela dessine des demi-cercles collés les uns aux autres de façon à créer des lignes représentant des vagues
def dessineVague() :
    a=0
    goto(0,0)
    up()
    goto((-window_width()),(window_height()-(50*a))) #on commence à dessiner en haut à gauche
    down()
    pencolor("white") #couleur des vagues
    while a<25 :
        up()
        goto((-window_width()-100),(window_height()-(50*a)))
        down()
        i=0
        while i<12 : #dessine une ligne de vague
            right(90)
            circle(60,180)
            left(180)
            circle(60,180)
            right(90)
            i=i+1
        a=a+1
    
#dessine un triangle permettant de dessiner le corps et la queue des poissons
def dessineTriangle(longueurCote,couleur,x,y) :
    # mise en place au point (x,y)
    up()
    goto(x,y)
    down()
    # mise en place de la couleur
    color(couleur)
    fillcolor(couleur)
    begin_fill()
    # on trace les côtés
    k = 0
    while k<3:
        right(360/3)
        forward(longueurCote)
        k=k+1
    end_fill()
# fin de la fonction dessinePolygone

#dessine les 2 poissons
def dessinePoissons() :
    #dessine le 1èr poisson
    dessineTriangle(50,"#f46542",-300,-300)
    right(60)
    dessineTriangle(70,"#f46542",-230,-300) #dessine les 2 triangles
    #dessine la tête
    begin_fill()
    goto(-230,-300)
    right(110)
    right(160)
    circle(35,180)
    end_fill()

    #dessine le 2ème poisson
    dessineTriangle(50,"#f46542",300,300)
    right(200)
    dessineTriangle(70,"#f46542",300,300) #dessine les 2 triangles
    #dessine la tête
    begin_fill()
    right(180)
    forward(70)
    left(30)
    circle(35,180)
    end_fill()
    #fin du dessin des 2 poissons

#la procédure dessineDecor dessine le décor final
#elle est appelée par le programme principal jeudesallumettes.py
def dessineDecor() :
    speed(0)
    tracer(0)
    up()
    goto(0,0)
    down()
    bgcolor("#8ab4f7") #couleur de fond
    dessineVague() #dessine les vagues
    dessinePoissons() #dessine les 2 poissons
