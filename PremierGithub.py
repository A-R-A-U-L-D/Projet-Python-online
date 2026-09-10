from turtle import *
from math import *
from random import randrange
def carre(taille,couleur,angle):
     color(couleur)
     c=0
     right(angle)
     while c<4:
          forward(taille)
          right(90)
          c+=1

def triangle(taille,couleur,angle):
     color(couleur)
     t=0
     setheading(angle)
     while t<3:
          forward(taille)
          left(120)
          t+=1

def etoile5(taille,couleur,angle):
     color(couleur)
     e=0
     right(angle)
     while e<5:
          forward(taille)
          right(144)
          e+=1
def etoile6(taille,couleur,angle):
     color(couleur)
     triangle(taille,couleur,angle)
     hauteur=(sqrt(3)*taille)/2
     up()
     setheading(angle+90)
     goto(xcor(),ycor()+(2/3)*hauteur)
     down()
     triangle(taille,couleur,angle+180)



