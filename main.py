from linearEq.directMethods.choleski import Choleski
from linearEq.directMethods.gauss import Gauss
from linearEq.directMethods.gaussJordan import GaussJordan
from linearEq.directMethods.crout import Crout
from linearEq.directMethods.doolittle import Doolittle
from linearEq.directMethods.thomas import Thomas
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel
from interpolation.interpolation import Interpolation
from interpolation.lagrange import Lagrange
from interpolation.newton import Newton
from interpolation.moindreCarre import MoindreCarre

# Methods directs
chski = Choleski("matrix.txt")
gauss = Gauss("matrix.txt")
gaussJ = GaussJordan("matrix.txt")
thomas = Thomas("matrix.txt")
doolittle = Doolittle("matrix.txt")
crout = Crout("matrix.txt")

"""print("\n\t-****** Méthodes Directs ******-\n")
print("-- Gauss: ", gauss.solution())
print("-- GaussJordan: ", gaussJ.solution())
print("-- Doolittle: ", doolittle.solution())
print("-- Crout: ", crout.solution())
print("-- Thomas: ", thomas.solution())
print("-- Choleski: ", chski.solution())"""

# Methods iteratives

jkb = jacobi("matrix.txt")
gs = gaussSeidel("matrix.txt")

"""print("\n\t-****** Méthodes Itératives ******-\n")
print("-- Jacobi: ", jkb.solution())
print("-- Gauss-seidel: ", gs.solution())"""

# interpolation
interpolation = Interpolation("interpolation.txt")



newton = Newton("interpolation.txt")
lagrange = Lagrange("interpolation.txt")
moindreCarre = MoindreCarre("interpolation.txt", 5)
""""intterpolation = Interpolation("interpolation.txt")
"""
