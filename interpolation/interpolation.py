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
from interpolation.polynom import Polynom
from interpolation.polynome import Polynome
from linearEq.utils.gaussForVal import gauss
from math import pow, exp


class Interpolation:

    def __init__(self, file):
        self.file = file
        self.polyN = None
        self.polyL = None
        self.polyM = None
        try:
            sys.stdin = open(join(dirname(__file__), self.file))
            self.X = [float(i) for i in sys.stdin.readline().split()]
            self.Y = [float(i) for i in sys.stdin.readline().split()]

            if len(self.X) != len(self.Y):
                print("Vos tableaux ne sont pas de meme taille")
            else:
                self.X = [k for k in self.X]
                self.Y = [k for k in self.Y]
                self.dim = len(self.X)
                Xval = np.arange(-3, 3, 0.1)

                vals = list()
                for i in range(self.dim):
                    vals.append([self.X[i], self.Y[i]])
                # self.polynomeLagrange(vals)

                self.polyN = self.newton()
                self.polyL = self.lagrange()
                self.polyM = self.moindreCarre(4)

                print("\n\t-****** Interpolation ******-\n")
                print("Newton:",self.polyN)
                print("Lagrange:",self.polyL)
                print("Moindre carre:",self.polyM)

                plt.plot(np.arange(-3, 3, 0.1), self.calcLagrange(np.arange(-3, 3, 0.1)), label='Courbe lagrange (C1)', c='blue')

                plt.plot(Xval, self.calcNewton(Xval), label='Courbe newton (C2)', c='green')

                plt.plot(Xval, self.calcMoindreCarre(Xval), label='Courbe moindreCarre (C3)', c='red')

                plt.plot(np.arange(-3, 3, 0.1), self.givenFunc(np.arange(-3, 3, 0.1), "(x**3 - 1)/(x**2 + 1)"), label='Courbe', c='black')

                # plt.scatter(self.X, self.Y, c='coral', label='Points')
                plt.title("Interpolation:\nPx1 = {}\nPx2 = {}\nPx3 = {}".format(self.polyL, self.polyN, self.polyM))
                plt.xlabel("X")
                plt.ylabel("Y")
                # plt.xticks(np.arange(-30, 30, 2))
                plt.legend()
                plt.show()
        except ValueError:
            print("Valeurs mal définies")

    """ ===================================================================== """
    def newton(self):
        matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(i + 1):
                matrix[i][j] = self.calcN(j, self.X[i])
        Coefs = gauss(matrix, self.Y).showResult()
        f = [0]
        for i in range(self.dim):
            f1 = [Coefs[i]]
            for j in range(i):
                f1 = Polynom().mult(f1, [ -self.X[j], 1])
            f = Polynom().add(f, f1)
        # print("zzzzz: ",Polynom().build(f))

        # Coefs[0] = -1
        polyN = Polynom().build(f)
        return polyN

    def calcN(self, dim, x):
        val = 1
        for i in range(dim):
            val = val * (x - self.X[i])
        return val

    def calcNewton(self, x):
        return eval(self.polyN)

    """ ===================================================================== """
    def lagrange(self):
        Px = [0]
        for i in range(self.dim):
            fi = [1]
            for j in range(self.dim):
                if i != j:
                    Dnmteur = self.X[i] - self.X[j]
                    fi = Polynom().mult(P1=fi, P2=[-self.X[j]/Dnmteur, 1 / Dnmteur])
                    # fi * (x - self.X[j]) / (self.X[i] - self.X[j])
            Px = Polynom().add(Px, Polynom().mult([self.Y[i]], fi))
            # print(Polynom().build(Px))
        # Px.reverse()
        """
        for i in range(len(Px)):
            if i != 0:
                Px[i] = Px[i] - Px[i]/5"""
        return Polynom().build(Px)

    def polynomeLagrange(self, listPoint) -> Polynome:
        n = len(listPoint) - 1
        P = Polynome(n, 0)
        X = [el[0] for el in listPoint]
        fX = [el[1] for el in listPoint]
        for i in range(n + 1):
            Oi = Polynome(0, 1)
            for j in range(n + 1):
                if (j != i): Oi *= Polynome([-X[j] / (X[i] - X[j]), 1 / (X[i] - X[j])])
            P += fX[i] * Oi
        print(P)
        return P

    def calcLagrange(self, x):
        return eval(self.polyL)

    def givenFunc(self, x, poly):
        return eval(poly)
        # return exp(x-1)/exp(x+1)

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
        Coefs.reverse()
        return Polynom().build(Coefs)

    def calcMoindreCarre(self, x):
        return eval(self.polyM)

