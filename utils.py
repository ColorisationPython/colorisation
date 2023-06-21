import numpy as np
from numpy import *
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

# pays: xmin ymin xmax ymax

# carte: matrice Numpy largeur x hauteur


def colorier(carte, pays, couleur):
    xmin, ymin, xmax, ymax = pays
    carte[xmin:xmax, ymin:ymax] = couleur


def valeurs_voisines(carte, pays):
    xmin, ymin, xmax, ymax = pays
    largeur, hauteur = shape(carte)
    valeurs = set()
    if xmin > 0:
        valeurs = valeurs | set(carte[xmin - 1, ymin:ymax])
    if xmax < largeur:
        valeurs = valeurs | set(carte[xmax, ymin:ymax])
    if ymin > 0:
        valeurs = valeurs | set(carte[xmin:xmax, ymin - 1])
    if ymax < hauteur:
        valeurs = valeurs | set(carte[xmin:xmax, ymax])
    return list(valeurs)



RED = 0.9
BLUE = 0.0
GREEN = 0.55
YELLOW = 0.65

pays1 = [0, 0, 200, 200]
pays2 = [200, 0, 400, 200]
pays3 = [0, 200, 200, 400]
pays4 = [200, 200, 400, 400]


def trier(liste_de_pays):
    return list(sorted(liste_de_pays, key=lambda pays: (pays[1], pays[2])))


def carte1():
    carte = empty((400, 400), dtype=float)
    colorier(carte, pays1, RED)
    colorier(carte, pays2, BLUE)
    colorier(carte, pays3, GREEN)
    colorier(carte, pays4, YELLOW)
    return carte


def test():
    c = carte1()

    print(valeurs_voisines(c, pays1))
    print(valeurs_voisines(c, pays2))
    print(valeurs_voisines(c, pays3))
    print(valeurs_voisines(c, pays4))

    imshow(c, cmap=matplotlib.cm.jet, vmin=0.0, vmax=1.0, interpolation="nearest")
    colorbar()
    show()
