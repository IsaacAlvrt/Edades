#Pi Approximation with a circle
import numpy as np
import matplotlib.pyplot as plt

circlex = []
circley = []

squarex = []
squarey = []

n = 10000
i = 1
while i <= n:
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)

    if x**2 + y**2 <= 1:
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i += 1

#Result
Pi = 4* len(circlex)/float(n)
print("Pi is approximately:", Pi)
print("\nPi is actually", np.pi)


#Graph
plt.title("Circle", fontsize="14")
plt.scatter(circlex,circley, color="blue")
plt.scatter(squarex,squarey, color="red")
plt.grid()
plt.show()
