import numpy as np

v1 = np.array([1,2,3])
v2 = np.array([2,3,4])

def dotProduct(a,b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
    return total

x = dotProduct(v1,v2)
print(x)
print("lazy = ",np.dot(v1,v2) )
