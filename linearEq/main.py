from gaussJordan import gaussJordan
from LU import LU
from choleski import choleski
from inverse import invert
from jacobi import jacobi
from gaussSeidel import gaussSeidel
jacobi = jacobi("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
#print(jacobi.solution())

gaussS = gaussSeidel("/home/totorino/Bureau/CIC Semestre3/MTH300/mth 300 algo numérique/codes/eqLineaire/linearEq/matrix.txt")
print(gaussS.solution())