from gaussJordan import gaussJordan
from gaussJordan import gaussJordan
from LU import LU
from choleski import choleski
from inverse import invert
# test of gaus-Jordan method
"""
alGaussJ1 = LU("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
alGaussJ.showMatrixL()
print()
alGaussJ.showMatrixU()
print(alGaussJ1.solution())
"""

#alGaussJ = gaussJordan("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
#alGaussJ.showResult()
alGaussJ = invert("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")

alGaussJ.invert()

