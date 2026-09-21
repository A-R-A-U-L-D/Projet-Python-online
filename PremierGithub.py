from turtle import *
from math import *

speed(3)
def carre(taille,couleur,angle):
     color(couleur)
     c=0
     right(angle)
     while c<4:
          forward(taille)
          right(90)
          c+=1

def triangle(taille,couleur,sens: bool=True ):
     color(couleur)
     t, k=0, 1
     if sens:
         k = 1
     else:
          k = -1
     while t<3:
          forward(taille)
          left(k*120)
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
     triangle(taille,couleur)
     hauteur=(sqrt(3)*taille)/2
     up()
     goto(xcor(),ycor()+(2/3)*hauteur)
     down()
     triangle(taille,couleur, sens=False)



