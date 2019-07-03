#Run with Jupyter / Spyder
from sympy.interactive import printing
printing.init_printing(use_latex = True)

import sympy as sp
import numpy as np

#Function
x = sp.Symbol("x")
func = sp.Function("func")
func = sp.sin(x)
#Integral
print("\nIntegral:")
inte = sp.Integral(func,x)
display(inte)

#Solve integral
answer = sp.integrate(func,x)
display(answer)

#Derivative
print("\nDerivative:")
deriv = sp.diff(func,x)
display(deriv)