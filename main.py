from linearEq.directMethods.choleski import Choleski
from linearEq.directMethods.gauss import Gauss
from linearEq.directMethods.gaussJordan import GaussJordan
from linearEq.directMethods.crout import Crout
from linearEq.directMethods.Doulit import Doulit
from linearEq.directMethods.thomas import Thomas
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel
from interpolation.interpolation import Interpolation

# from scipy.linalg import lu

# Methods directs
# chski = Choleski("matrix.txt")
gauss = Gauss("matrix.txt")
gaussJ = GaussJordan("matrix.txt")
thomas = Thomas("matrix.txt")
doulit = Doulit("matrix.txt")
crout = Crout("matrix.txt")

print("Gauss ", gauss.solution())
print("Thomas ", thomas.solution())
print("GaussJordan ", gaussJ.solution())
print("Doulit ", doulit.solution())
# print("Choleski", chski.solution())


# Methods iteratives
jkb = jacobi("matrix.txt")
gs = gaussSeidel("matrix.txt")

# interpolation
# interpolation = Interpolation("interpolation.txt")


print("Jacobi ", jkb.solution())
print("Gauss-seidel ", gs.solution())

"""
newton = Newton("interpolation.txt")
lagrange = Lagrange("interpolation.txt")
moindreCarre = MoindreCarre("interpolation.txt", 5)
intterpolation = Interpolation("interpolation.txt")
"""
