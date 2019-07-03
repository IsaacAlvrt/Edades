import matplotlib.pyplot as plt
import numpy as np


#Variables
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,14,12,20,21,17,29,24,31,32,45]

#Regresion
reg = np.polyfit(x,y,1)

#Coeficientes
constante = len(reg) -1
print( round(reg[constante],5), "= Constante")

for i in range(0, len(reg) -1 ):
    print( round(reg[i],5), "= Coeficiente no.", i +1 )

#grafica
plt.scatter(x,y, color = "gray")
plt.plot(x, np.polyval(reg,x) )
plt.title("Grafica", fontsize = 18)
plt.xlabel("X axis", fontsize = 15)
plt.ylabel("Y axis", fontsize = 15)
plt.show()
