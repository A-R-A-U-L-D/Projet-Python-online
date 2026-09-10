from turtle import *
def etoile_5(couleur,taille,angle):
    color(couleur)
    e=0
    while e<5:
        rotation=180-180/5
        forward(taille)
        left(rotation)
        e+=1
    

