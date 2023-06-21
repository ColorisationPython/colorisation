#Algo de coloriage et affichage de carte

#récupération des données pour test affichage
from numpy import *
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

#Récupération de la carte :
from Carte import carte

#récupération de la matrice de données triée
from Donnees import Dt

#Récupération de la méthode valeurs voisines:
from utils import valeurs_voisines

#Récupération de la méthode de coloriage
from utils import colorier

#Définition des couleurs
RED = 0.9
BLUE = 0.1
GREEN = 0.55
YELLOW = 0.65

l=len(Dt)
print(l)

#def algo_coloriage(Dt)

#Coloriage du 1er pays en rouge:
xmin=Dt[0,0]
ymin=Dt[0,1]
xmax=Dt[0,2]
ymax=Dt[0,3]
pays=[xmin,ymin,xmax,ymax]
colorier(carte,pays,RED)    

for i in range (1,l):
#Définition du pays de travail
    xmin=Dt[i,0]
    ymin=Dt[i,1]
    xmax=Dt[i,2]
    ymax=Dt[i,3]
    pays=[xmin,ymin,xmax,ymax]
    V=sorted(valeurs_voisines(carte,pays))
    print(V)
    # for j in range (len(V))
    if V==[0.0] :
        colorier(carte,pays,RED)
    elif V==[0.0,0.9] or V==[0.0,0.65,0.9] or V==[0.0,0.55,0.9] or V==[0.0,0.55,0.65,0.9]:
        # or V==[0.9,0.0]:
        colorier(carte,pays,BLUE)
    elif V==[0.0,0.1] or V==[0.0,0.55] or V== [0.0,0.65] or V==[0.0,0.1,0.55] or V==[0.0,0.1,0.65] or V==[0.0,0.1,0.55,0.65] or V==[0.0,0.55,0.65]:
        colorier(carte,pays,RED)
    elif V==[0.0,0.1,0.9] or V==[0.0,0.1,0.65,0.9] :
        # or V==[0.0,0.9,0.1] or V==[0.1,0.0,0.9] or V==[0.1,0.9,0.0]:
        colorier(carte,pays,GREEN)
    elif V==[0.0,0.1,0.55,0.9] :
        # or V==[0.0,0.1,0.9,0.55] or V==[0.0,0.55,0.9,0.1] or V==[0.0,0.55,0.1,0.9] or V==[0.0,0.9,0.55,0.1] or V==[0.0,0.9,0.1,0.55] or V==[0.1,0.0,0.55,0.9]
        colorier(carte,pays,YELLOW)

# print(carte)

#Test de l'affichage de la carte
imshow(carte, cmap=matplotlib.cm.jet, vmin=0.0, vmax=1.0, interpolation="nearest")
colorbar()
show() 

