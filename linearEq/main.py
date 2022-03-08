from linearEq.directMethods.choleski import Choleski
from linearEq.directMethods.gauss import Gauss
from linearEq.directMethods.gaussJordan import GaussJordan
from linearEq.directMethods.crout import Crout
from linearEq.directMethods.Doulit import Doulit
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel
from scipy.linalg import lu
import numpy as np
### Methods directs
chski = Choleski("matrix.txt")
gauss = Gauss("matrix.txt")
gaussJ = GaussJordan("matrix.txt")
doulit = Doulit("matrix.txt")
crout = Crout("matrix.txt")

print("Gauss ", gauss.solution())
print("GaussJordan ", gaussJ.solution())
print("Crout ", crout.solution())
print("Doulit ", doulit.solution())
print("Choleski", chski.solution())

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