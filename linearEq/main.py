from gaussJordan import gaussJordan
from gauss import gauss
from LU import LU

# test of gaus-Jordan method
alGaussJ1 = LU("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
"""alGaussJ.showMatrixL()
print()
alGaussJ.showMatrixU()"""

print(alGaussJ1.solution())

alGaussJ = gauss("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")

alGaussJ.showResult()
