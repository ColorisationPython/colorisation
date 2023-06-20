from utils import colorier, valeurs_voisines
from utils import RED, BLUE, GREEN, YELLOW

from numpy import *
import matplotlib
from matplotlib.pyplot import *

largeur, hauteur = 600, 400
carte = empty((largeur, hauteur), dtype=float)
pays1 = [50, 50, 200, 100]  # xmin ymin xmax ymax
pays2 = [50, 100, 200, 150]  # xmin ymin xmax ymax

colorier(carte, pays1, RED)
colorier(carte, pays2, GREEN)
print(valeurs_voisines(carte, pays1))
print(valeurs_voisines(carte, pays2))


imshow(carte.T, cmap=matplotlib.cm.jet, vmin=0.0, vmax=1.0, interpolation="nearest")
colorbar()
show()
