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
        self.coefs = None
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
            Xval = np.arange(-20, 30, 0.5)
            Yval = list()
            Yval2 = list()
            Y2 = list()

            for i in X:
                Y2.append(self.calc(i))
            for i in Xval:
                Yval.append(self.calc(i))
                Yval2.append(self.givenFunc(i))

            plt.plot(Xval, Yval, label='Courbe obtenue')
            plt.plot(Xval, Yval2, label='Courbe', c='red')
            plt.scatter(X, Y2, c='coral', label='Points')
            plt.title("Interpolation de Lagrange\nPx = {}".format(self.poly))
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.show()

    def func(self):
        Px = [0]
        for i in range(self.dim):
            fi = [1]
            for j in range(self.dim):
                if i != j:
                    Dnmteur = self.X[i] - self.X[j]
                    fi = Polynom().mult(P1=fi, P2=[self.X[j]/Dnmteur, 1/Dnmteur])
                    # fi * (x - self.X[j]) / (self.X[i] - self.X[j])
            Px = Polynom().add(Px, Polynom().mult([self.Y[i]], fi))
        return Px

    def calc(self, X):
        self.coefs = self.func() # [round(x, 2) for x in self.func()]
        self.coefs.reverse()
        self.poly = Polynom().build(self.coefs)
        return eval(self.poly)

    def givenFunc(self, X):
        return eval("((1/3)*X**3)+(X**2)-(3/4*X)")
