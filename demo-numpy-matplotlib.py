from numpy import *
from numpy import array, zeros, empty  # Importez toutes les fonctionalités de numpy
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

RED = 1.0
BLUE = 0.0
GREEN = 0.55


matrix = empty((400, 400))
matrix[0:400, 0:400] = BLUE
matrix[0:200, 0:200] = RED
matrix[200:400, 200:400] = GREEN
imshow(matrix, cmap=matplotlib.cm.jet, interpolation="nearest")
colorbar()
show()
