from gaussJordan import gaussJordan
from LU import LU
from choleski import choleski
from inverse import invert

alGaussJ1 = LU("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
alGaussJ1.showMatrixL()
print()
alGaussJ1.showMatrixU()
print(alGaussJ1.solution())
"""

#alGaussJ = gaussJordan("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
#alGaussJ.showResult()
alGaussJ = choleski("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")

alGaussJ.triangularize()
alGaussJ.showMatrixU()
print()
alGaussJ.showMatrixL()
print(alGaussJ.solution())"""

