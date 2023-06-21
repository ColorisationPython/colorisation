import sys
import numpy as np
from numpy import array,zeros
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

#Récupération de la matrice D de Donnees
from Donnees import D

Max =np.max(D)
#print(Max)

carte=np.zeros((Max,Max))
#print(Carte)