#Interface graphique de dessin des anneaux olympiques 
from tkinter import *
#definition des fonctions pour les anneaux olympiques
def dessiner_anneau(i):
    x1,y1,x2,y2=coordonnées[i][0],coordonnées[i][1],coordonnées[i][2],coordonnées[i][3]
    can.create_oval(x1,y1,x2,y2,outline=couleur[i])*

def anneau_bleu():
    dessiner_anneau(0)
def anneau_noir():
    dessiner_anneau(1)
def anneau_rouge():
    dessiner_anneau(2)
def anneau_jaune():
    dessiner_anneau(3):
def anneau_vert():
    dessiner_anneau(4)

#Coordonnées et couleur des anneaux
coordonnées=[[10,10,60,10],[65,10,115,10],[120,10,170,10],[30,30,80,30],[85,30,135,30]]
couleur=["blue","black","red","yellow","green"]

#Creation de l'interface graphique
fen=Tk()
can=Canvas(fen,bg="white",height=200,width=200)
can.pack()
bou=Button(fen,text="Quitter",command=fen.quit)
bou.pack(side=RIGHT)
#Boutton des 05 anneaux
Button(fen,text="bleu",command=anneau_bleu).pack(side=TOP)
Button(fen,text="Noir",command=anneau_noir).pack(side=TOP)
Button(fen,text="Rouge",command=anneau_rouge).pack(side=TOP)
Button(fen,text="Jaune",command=anneau_jaune).pack(side=BOTTOM)
Button(fen,text="Vert",command=anneau_vert).pack(side=BOTTOM)*

fen.mainlopp()
fen.destroy()
