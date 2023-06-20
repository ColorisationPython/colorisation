from utils import colorier, valeurs_voisines, trier
from utils import RED, BLUE, GREEN, YELLOW

from numpy import *
import matplotlib
from matplotlib.pyplot import *

file = open("Cartes/Carte_0.txt", "r", encoding="utf-8")

liste_de_pays = []
for line in file.read().splitlines():
    if line.strip() != "":
        nom, xmin, ymin, xmax, ymax = line.split()
        liste_de_pays.append([int(xmin), int(ymin), int(xmax), int(ymax)])

largeur = max(pays[2] for pays in liste_de_pays)
hauteur = max(pays[3] for pays in liste_de_pays)

carte = empty((largeur, hauteur), dtype=float)

liste_de_pays = trier(liste_de_pays)

n = len(liste_de_pays)
for i, pays in enumerate(liste_de_pays):
    colorier(carte, pays, i / n)

imshow(carte.T, cmap=matplotlib.cm.jet, vmin=0.0, vmax=1.0, interpolation="nearest")
colorbar()
show()
