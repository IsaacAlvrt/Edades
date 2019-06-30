import matplotlib.pyplot as plt

#Read file
f = open("edades.txt")
file = f.readlines()
n = []

#Create array with integers in file
for i in file:
    n.append(int(i))


#Boxplot
plt.boxplot(n, vert = False, patch_artist = True)
plt.title("Edades de estudiantes encuestados.")
plt.xlabel("Edades")
plt.show()
