#Amelioration du tri

#Tri des pays par nombre de voisin

#Récupération de la carte :
from Carte import carte

#récupération de la matrice de données triée
from Donnees import Dt

#Récupération du nombre de pays
from Donnees import l

#Récupération de la méthode valeurs voisines:
from utils import valeurs_voisines

#Récupération de la méthode de coloriage
from utils import colorier

#Initialisation du vecteur "couleur des voisins"
pays=[Dt[0,0],Dt[0,1],Dt[0,2],Dt[0,3]]
V=sorted(valeurs_voisines(carte,pays))

#coloriage de tous les pays d'une couleur différentes
for i in range (1,l):
#Définition du pays de travail
    xmin=Dt[i,0]
    ymin=Dt[i,1]
    xmax=Dt[i,2]
    ymax=Dt[i,3]
    pays=[xmin,ymin,xmax,ymax]
    c=i/(l+1)
    colorier(carte,pays,c)
    
    #Comparason du nombre de voisin en fonction des couleurs avoisinantes :
    
    # if len(sorted(valeurs_voisines(carte,pays))) > len(V) :
    #     T=[xmin,ymin,xmax,ymax]
    #     Dt[i-1,:]=Dt[i,:]
    #     Dt[i,:]=T
    #plus V est long plus le pays a de voisins
    
Dt = [list(x) for x in Dt]
# print(Dt)

def key(pays):
    #print(valeurs_voisines(carte, pays))
    return -len(valeurs_voisines(carte, pays))

Dt.sort(key=key)
print(Dt)
    