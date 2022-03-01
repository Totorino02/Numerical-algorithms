from gaussJordan import gaussJordan
from LU import LU
from choleski import choleski
from inverse import invert
from jacobi import jacobi
from gaussSeidel import gaussSeidel
from lagrange import lagrange
import numpy as np
import matplotlib.pyplot as pt
x = np.arange(0, 5, 0.1)
y = np.sin(x)
pt.plot([1,2,3],[2,4,6])
pt.show()


#lg = lagrange()