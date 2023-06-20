from numpy import *
from numpy import array, zeros # Importez toutes les fonctionalités de numpy
import matplotlib
from matplotlib.pyplot import imshow, show, colorbar

# Attention: valeurs qui ne marchent que pour la colormap matplotlib.cm.jet !!!
RED = 1.0
BLUE = 0.0
GREEN = 0.55


zero_matrix = zeros((400, 400))
zero_matrix[0:200, 0:200] = RED
zero_matrix[200:400, 200:400] = GREEN
#print(zero_matrix)
imshow(zero_matrix, cmap=matplotlib.cm.jet, interpolation='nearest')
colorbar()
show()
