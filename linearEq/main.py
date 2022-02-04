from gaussJordan import gaussJordan
from gauss import gauss

# test of gaus-Jordan method
alGaussJ = gauss("./matrix.txt")
alGaussJ.triangularize()
alGaussJ.showTM()
