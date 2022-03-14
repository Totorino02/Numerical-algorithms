"""
    Name: lagrange.py
    Goal: Numerical resolution of linear equations using the method of jacobi
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 24/02/2022
"""
import numpy as np
import matplotlib.pyplot as plt
from linearEq.interpolation.polynom import Polynom
import sys
from os.path import dirname, join


class Lagrange:

    def __init__(self, file):
        self.poly = None
        self.file = file
        sys.stdin = open(join(dirname(__file__), self.file))
        X = [float(i) for i in sys.stdin.readline().split()]
        Y = [float(i) for i in sys.stdin.readline().split()]

        if len(X) != len(Y):
            print("Vos tableaux ne sont pas de meme taille")
        else:
            self.X = [k for k in X]
            self.Y = [k for k in Y]
            self.dim = len(X)
            Xval = np.arange(-30, 30, 0.5)
            Y2 = list()
            self.poly = self.funcLagrange()
            for i in X:
                Y2.append(self.calcLagrange(i))

            plt.plot(Xval, self.calcLagrange(Xval), label='Courbe obtenue')
            plt.plot(np.arange(-5, 5, 0.1), self.givenFunc(np.arange(-5, 5, 0.1), "X**2 + 1"), label='Courbe',c='black')
            plt.scatter(X, Y2, c='coral', label='Points')
            plt.title("Interpolation de Lagrange\nPx = {}".format(self.poly))
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.show()

    def funcLagrange(self):
        Px = [0]
        for i in range(self.dim):
            fi = [1]
            for j in range(self.dim):
                if i != j:
                    Dnmteur = self.X[i] - self.X[j]
                    fi = Polynom().mult(P1=fi, P2=[self.X[j] / Dnmteur, 1 / Dnmteur])
                    # fi * (x - self.X[j]) / (self.X[i] - self.X[j])
            Px = Polynom().add(Px, Polynom().mult([self.Y[i]], fi))
            # print(Polynom().build(Px))
        return Polynom().build(Px)

    def calcLagrange(self, X):
        return eval(self.poly)

    def givenFunc(self, X, poly):
        return eval(poly)

