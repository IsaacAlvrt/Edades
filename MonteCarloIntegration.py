from scipy import random
import numpy as np
import matplotlib.pyplot as plt

#Limits of integration (a,b)
a = 0
b = np.pi
n = 1000

#Function f(x) = sin(x)
def f(x):
    return np.sin(x)

areas = []
for i in range(n):
    #Random numbers in range(a,b)
    xrand = np.zeros(n)
    for i in range(n):
        xrand[i] = random.uniform(a,b)

    #Integral
    dots = 0.0
    for i in range(n):
        dots += f(xrand[i])

    integral = (b-a)/float(n) * dots
    areas.append(integral)

#Result
print("The integral is", np.mean(areas))
print("The standar deviation is", np.std(areas))

#Histogram
plt.hist(areas, bins=25, ec = "black", color="lightblue")
plt.title("Distribution of areas calculated")
plt.show()
