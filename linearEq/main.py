from linearEq.directMethods.choleski import choleski
from linearEq.directMethods.gauss import gauss
from linearEq.directMethods.gaussJordan import gaussJordan
from linearEq.directMethods.LU import LU
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel
from scipy.linalg import lu
import numpy as np
### Methods directs
chski = choleski("matrix.txt")
gauss = gauss("matrix.txt")
gaussJ = gaussJordan("matrix.txt")
Lu = LU("matrix.txt")

print(gauss.solution())
print(gaussJ.solution())
print(Lu.solution())
print(chski.solution())

### Methods iteratives
jkb = jacobi("matrix.txt")
gs = gaussSeidel("matrix.txt")
#print(jkb.solution())
#print(gs.solution())

A = np.array([
[1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0],
[2.0, 1.0, 0.0, 1.0, 2.0, 1.0, 2.0],
[0.0, 1.0, 2.0, 3.0, 4.0, 0.0, 0.0],
[0.0, 1.0, 2.0, 3.0, 4.0, 1.0, 0.0],
[3.0, 2.0, 1.0, 0.0, 1.0, 1.0, 3.0],
[1.0, 0.0, 1.0, 2.0, 3.0, 1.0, 1.0],
[4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 4.0],
])
P, L, U = lu(A)
"""
print(P)
print()
print(L)
print()
print(U)
"""


B = [0.0, 1.0, 0.0, 0.0, 2.0, 1.0, 2.0]