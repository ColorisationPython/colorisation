#Algo de coloriage et affichage de carte

#récupération des données pour test affichage
from numpy import *
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

#Récupération de la carte :
from Carte import carte

#récupération des matrices de données triées
from Donnees import Dt
from TriAmeliore import Dt1


#Récupération de la méthode valeurs voisines:
from utils import valeurs_voisines

#Récupération de la méthode de coloriage
from utils import colorier

#Récupération des indices d'erreur du comparateur de tri:
from ComparaisonTris import e,e1

#Définition des couleurs
RED = 0.9
BLUE = 0.1
GREEN = 0.55
YELLOW = 0.65

if e<=e1 :
    D=Dt
else :
    D=Dt1

l=len(D)
print(l)


#Coloriage du 1er pays en rouge:
xmin=D[0,0]
ymin=D[0,1]
xmax=D[0,2]
ymax=D[0,3]
pays=[xmin,ymin,xmax,ymax]
colorier(carte,pays,RED)    

for i in range (1,l):
#Définition du pays de travail
    xmin=D[i,0]
    ymin=D[i,1]
    xmax=D[i,2]
    ymax=D[i,3]
    pays=[xmin,ymin,xmax,ymax]
    V=sorted(valeurs_voisines(carte,pays))
    print(V)
    
    if V==[0.0] :
        colorier(carte,pays,RED)
    elif V==[0.0,0.9] or V==[0.0,0.65,0.9] or V==[0.0,0.55,0.9] or V==[0.0,0.55,0.65,0.9] or V==[0.55,0.9] or V==[0.55,0.65,0.9]:
        colorier(carte,pays,BLUE)
    elif V==[0.0,0.1] or V==[0.0,0.55] or V== [0.0,0.65] or V==[0.0,0.1,0.55] or V==[0.0,0.1,0.65] or V==[0.0,0.1,0.55,0.65] or V==[0.0,0.55,0.65] or V==[0.1,0.65] or V==[0.1,0.55,0.65]:
        colorier(carte,pays,RED)
    elif V==[0.0,0.1,0.9] or V==[0.0,0.1,0.65,0.9] or V==[0.1,0.65,0.9] or V==[0.1,0.9] or V==[0.1,0.65,0.9]:
        colorier(carte,pays,GREEN)
    elif V==[0.0,0.1,0.55,0.9] or V==[0.1,0.55,0.9] :
        colorier(carte,pays,YELLOW)

#Test de l'affichage de la carte
imshow(carte.T, cmap=matplotlib.cm.jet, vmin=0.0, vmax=1.0, interpolation="nearest")
colorbar()
show() 

