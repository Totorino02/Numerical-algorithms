from linearEq.directMethods.choleski import Choleski
from linearEq.directMethods.gauss import Gauss
from linearEq.directMethods.gaussJordan import GaussJordan
from linearEq.directMethods.crout import Crout
from linearEq.directMethods.Doulit import Doulit
from linearEq.iterativeMethods.jacobi import jacobi
from linearEq.iterativeMethods.gaussSeidel import gaussSeidel
from linearEq.interpolation.newton import Newton
from linearEq.interpolation.lagrange import Lagrange
from linearEq.interpolation.moindreCarre import MoindreCarre
from linearEq.interpolation.interpolation import Interpolation
from scipy.linalg import lu
import numpy as np

# Methods directs
chski = Choleski("matrix.txt")
gauss = Gauss("matrix.txt")
gaussJ = GaussJordan("matrix.txt")
doulit = Doulit("matrix.txt")
crout = Crout("matrix.txt")

"""
print("Gauss ", gauss.solution())
print("GaussJordan ", gaussJ.solution())
print("Doulit ", doulit.solution())
print("Choleski", chski.solution())
"""


# Methods iteratives
jkb = jacobi("matrix.txt")
gs = gaussSeidel("matrix.txt")

"""
print("Jacobi ", jkb.solution())
print("Gauss-seidel ", gs.solution())
"""

newton = Newton("interpolation.txt")
lagrange = Lagrange("interpolation.txt")
moindreCarre = MoindreCarre("interpolation.txt", 5)
intterpolation = Interpolation("interpolation.txt")

