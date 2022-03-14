"""
    name: interpolation.py
    Goal: resume all interpolation functions
    author: HOUNSI Madouvi antoine-sebastien
    date: 14/03/2022
"""
import sys
from os.path import dirname, join
import matplotlib.pyplot as plt
import numpy as np
from linearEq.interpolation.polynom import Polynom
from linearEq.utils.gaussForVal import gauss


class Interpolation:

    def __init__(self, file):
        self.file = file
        self.polyN = None
        self.polyL = None
        self.polyM = None
        sys.stdin = open(join(dirname(__file__), self.file))
        self.X = [float(i) for i in sys.stdin.readline().split()]
        self.Y = [float(i) for i in sys.stdin.readline().split()]

        if len(self.X) != len(self.Y):
            print("Vos tableaux ne sont pas de meme taille")
        else:
            self.X = [k for k in self.X]
            self.Y = [k for k in self.Y]
            self.dim = len(self.X)
            Xval = np.arange(-15, 15, 0.5)

            try:
                self.polyN = self.newton()
                self.polyL = self.lagrange()
                self.polyM = self.moindreCarre(3)
                print(self.polyN)
                print(self.polyL)
                print(self.polyM)
                plt.plot(np.arange(-20, 20, 0.1), self.calcLagrange(np.arange(-20, 20, 0.1)), label='Courbe lagrange', c='blue')
                plt.plot(Xval, self.calcNewton(Xval), label='Courbe newton', c='green')
                plt.plot(Xval, self.calcMoindreCarre(Xval), label='Courbe moindreCarre', c='red')
                plt.plot(np.arange(-10, 10, 0.1), self.givenFunc(np.arange(-10, 10, 0.1), "X**2 + 1"), label='Courbe', c='black')
                # plt.plot(np.arange(-30, 30, 2), np.zeros(30), c='black', linestyle='--')
                # plt.plot(np.zeros(300), np.arange(-300, 300, 2), c='black', linestyle='--')
                plt.scatter(self.X, self.Y, c='coral', label='Points')
                plt.title("Interpolation:\nPx1 = {}\nPx2 = {}\nPx3 = {}".format(self.polyL, self.polyN, self.polyM))
                plt.xlabel("X")
                plt.ylabel("Y")
                # plt.xticks(np.arange(-30, 30, 2))
                plt.legend()
                plt.show()

            except TypeError:
                print("Erreur lors du calcul veuillez réessayer")
            except ValueError:
                print("Valeurs mal définies")

    """ ===================================================================== """
    def newton(self):
        matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(i + 1):
                matrix[i][j] = self.calcN(j, self.X[i])
        Coefs = gauss(matrix, self.Y).showResult()
        polyN = Polynom().build(Coefs)
        return polyN

    def calcN(self, dim, x):
        val = 1
        for i in range(dim):
            val = val * (x - self.X[i])
        return val

    def calcNewton(self, X):
        return eval(self.polyN)

    """ ===================================================================== """
    def lagrange(self):
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
        return eval(self.polyL)

    def givenFunc(self, X, poly):
        return eval(poly)

    """ ===================================================================== """
    def moindreCarre(self, deg):
        deg = deg
        matrix = np.zeros((deg + 1, deg + 1))
        vect = list()
        maxDeg = 2 * deg

        # matrix
        for i in range(maxDeg, deg - 1, -1):
            for j in range(deg + 1):
                temp = [pow(self.X[k], i - j) for k in range(self.dim)]
                matrix[maxDeg - i][j] = sum(temp)

        # vector
        for i in range(deg, -1, -1):
            temp = [pow(self.X[k], i) * self.Y[k] for k in range(self.dim)]
            vect.append(sum(temp))
        Coefs = gauss(matrix, vect).showResult()
        return Polynom().build(Coefs)

    def calcMoindreCarre(self, X):
        return eval(self.polyM)

