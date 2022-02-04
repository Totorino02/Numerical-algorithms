from gaussJordan import gaussJordan
from gauss import gauss

# test of gaus-Jordan method
alGaussJ = gauss("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
alGaussJ.triangularize()
alGaussJ.showTM()
alGaussJ.showResult()
