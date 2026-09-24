from math import *
#Utilisation d'une fonction
def simuler_trajectoire(x0,y0,v0,alpha,x_cible,y_cible,rayon,Delta_t,t_max):
  #Initialisation des données
  g,t=9.81,0.00
  alpha_radian=radians(alpha)
  #Composantes de la vitesse
  v0x,v0y=v0*cos(alpha_radian),v0*sin(alpha_radian)
  x,y=x0,y0
  #Conservation des coordonées
  liste_x=[x0]
  liste_y=[y0]

  #Valeur du toucher de la cible
  touche= False
  temps_toucher=None
  
  while y>=0 and t<=t_max:
#Equations horaires du mouvement
    x=x0+v0x*t
    y=y0+v0y*t-0.5*g*(t**2)
    liste_x.append(x)
    liste_y.append(y)
    t+=Delta_t
   

#Evaluation de la condition du toucher du sol
    if t>0 and y<0:
      break
#Calcul de la distance entre le mobile et la cible
    distance= sqrt( (x_cible-x)**2 + (y_cible-y)**2 )

#Verification de la condition du toucher de la cible*
    if distance<=rayon:
      touche=True
      temps_toucher=t
      break
  #Retour des valeurs
  if touche:
      return touche,round(temps_toucher,2)
  else:
      return None

#Essai des cas pour verification

