#Comparaison des tris de donnée

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

#Définition des couleurs
RED = 0.9
BLUE = 0.1
GREEN = 0.55
YELLOW = 0.65

l=len(Dt)
# print(l)

#initialisation des compteurs
e=0
e1=0


#Test du tri normal 

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
    
#Extraction de V    
    V=sorted(valeurs_voisines(carte,pays))
    print(V)
    if V==[0.0] :
        colorier(carte,pays,RED)
    elif V==[0.0,0.9] or V==[0.0,0.65,0.9] or V==[0.0,0.55,0.9] or V==[0.0,0.55,0.65,0.9] or V==[0.55,0.9] or V==[0.55,0.65,0.9]:
        # or V==[0.9,0.0]:
        colorier(carte,pays,BLUE)
    elif V==[0.0,0.1] or V==[0.0,0.55] or V== [0.0,0.65] or V==[0.0,0.1,0.55] or V==[0.0,0.1,0.65] or V==[0.0,0.1,0.55,0.65] or V==[0.0,0.55,0.65] or V==[0.1,0.65] or V==[0.1,0.55,0.65]:
        colorier(carte,pays,RED)
    elif V==[0.0,0.1,0.9] or V==[0.0,0.1,0.65,0.9] or V==[0.1,0.65,0.9] or V==[0.1,0.9] or V==[0.1,0.65,0.9]:
        # or V==[0.0,0.9,0.1] or V==[0.1,0.0,0.9] or V==[0.1,0.9,0.0]:
        colorier(carte,pays,GREEN)
    elif V==[0.0,0.1,0.55,0.9] or V==[0.1,0.55,0.9] :
        # or V==[0.0,0.1,0.9,0.55] or V==[0.0,0.55,0.9,0.1] or V==[0.0,0.55,0.1,0.9] or V==[0.0,0.9,0.55,0.1] or V==[0.0,0.9,0.1,0.55] or V==[0.1,0.0,0.55,0.9]
        colorier(carte,pays,YELLOW)
    elif V==[0.0,0.1,0.55,0.65,0.9] or V==[0.1,0.55,0.65,0.9]:
        e=e+1
        
print("\n")


#Test du tri amélioré :

#Remise à  des couleurs des pays :
for i in range (0,l):
    xmin=Dt[i,0]
    ymin=Dt[i,1]
    xmax=Dt[i,2]
    ymax=Dt[i,3]
    pays=[xmin,ymin,xmax,ymax]
    colorier(carte,pays,0.0)
    
#Coloriage du 1er pays en rouge:
xmin=Dt1[0,0]
ymin=Dt1[0,1]
xmax=Dt1[0,2]
ymax=Dt1[0,3]
pays=[xmin,ymin,xmax,ymax]
colorier(carte,pays,RED)    

for i in range (1,l):
#Définition du pays de travail
    xmin=Dt1[i,0]
    ymin=Dt1[i,1]
    xmax=Dt1[i,2]
    ymax=Dt1[i,3]
    pays=[xmin,ymin,xmax,ymax]
    
#Extraction de V    
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
    elif V==[0.0,0.1,0.55,0.65,0.9] or V==[0.1,0.55,0.65,0.9]:
        e1=e1+1
        
print("e = ",e, "e1 = ",e1)

#Remise à  des couleurs des pays :
for i in range (0,l):
    xmin=Dt[i,0]
    ymin=Dt[i,1]
    xmax=Dt[i,2]
    ymax=Dt[i,3]
    pays=[xmin,ymin,xmax,ymax]
    colorier(carte,pays,0.0)