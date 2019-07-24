#Choukroun-Mittaine

from turtle import*

#la procédure dessineTortue dessine une tortue-allumette
#elle est appelée par le programme principal jeudesallumettes.py
#dessine le corps et la tête de la tortue-allumette
def dessineTortue(x):
    fillcolor("#6B8E23")
    pencolor("#6B8E23")
    begin_fill()
    left(30)
    forward(15)
    circle(50,120)
    right(60)
    forward(12.5)
    circle(12.5,180)
    forward(12.5)
    right(60)
    circle(50,120)
    forward(15)
    end_fill()

#dessine les 4 pattes de la tortue-allumette
    #1ère patte
    fillcolor("#CB7539")
    pencolor("#CB7539")    
    up()
    goto(11.5+x,5)
    down()
    begin_fill()
    right(20)
    forward(15)
    circle(5,180)
    forward(15)
    end_fill()

    #2ème patte
    fillcolor("#CB7539")
    pencolor("#CB7539")
    up()
    goto(-17.5+x,10)
    down()
    begin_fill()
    left(90)
    forward(15)
    circle(5,180)
    forward(18)
    end_fill()

    #3ème patte
    fillcolor("#CB7539")
    pencolor("#CB7539")
    up()
    goto(31+x,75)
    down()
    begin_fill()
    right(70)
    forward(30)
    circle(7.5,180)
    forward(30)
    circle(10,90)
    end_fill()

    #4ème patte
    fillcolor("#CB7539")
    pencolor("#CB7539")    
    up()
    goto(-24+x,85)
    down()
    begin_fill()
    right(125)
    circle(10,90)
    forward(30)
    circle(7.5,180)
    forward(32.5)
    end_fill()
