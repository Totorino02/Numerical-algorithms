from linearEq.directMethods.choleski import choleski
from linearEq.directMethods.gauss import gauss
from linearEq.directMethods.gaussJordan import gaussJordan
from linearEq.directMethods.LU import LU
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel

### Methods directs
chski = choleski("matrix.txt")
gauss = gauss("matrix.txt")
gaussJ = gaussJordan("matrix.txt")
lu = LU("matrix.txt")

chski.solution()

### Methods iteratives
jkb = jacobi("matrix.txt")
gs = gaussSeidel("matrix.txt")
print("GaussSeidel: ", gs.solution())
print("Jacobi: ", jkb.solution())