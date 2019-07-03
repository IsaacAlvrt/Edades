import numpy as np
import math

k=0
n=2
total = 0
while k <= n:
    factor = ( 2 * math.sqrt(2) ) / 9801
    num = math.factorial(4*k) * ( 1103 + (26390*k) )    #Numerator
    den = math.factorial(k)**4  * 396**(4*k)            #Denominator
    term = factor * num / den
    total += term
    Pi = 1/total
    k += 1
#Result
print("PI is approximately:", Pi)
print("\nPI actually is:", np.pi)
