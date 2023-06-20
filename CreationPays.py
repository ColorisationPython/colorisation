#Lecture du fichier carte
import sys
file = open("Carte_1.txt", "r", encoding="ascii")
f=file.read()
print(f)

#Transformation du fichier carte en une liste de caractères
d=f.replace(' ','\n').split()
print(d)
print("\n",len(d))

#Supression des "Pi"
l=int(len(d)/5)
print(l)
for i in range (0,4*l,4):
   del(d[i])
print(d)

#Transformation de ma liste de caractères en liste de nombres
dnum=list(map(int,d))
print(dnum)

#Transformation de ma liste en matrice D
def nest_list(liste,rows,columns):
       resultat=[]
       debut = 0
       fin = columns
       for i in range(rows):
           resultat.append(liste[debut:fin])
           debut +=columns
           fin += columns
       return resultat

D=nest_list(dnum,27,4)
print(D)


