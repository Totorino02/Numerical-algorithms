from gaussJordan import gaussJordan
from gauss import gauss
from LU import LU

# test of gaus-Jordan method
alGaussJ = LU("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
#alGaussJ.triangularize()
#alGaussJ.showTM()
alGaussJ.showMatrixL()
print()
alGaussJ.showMatrixU()

print(alGaussJ.solution())
