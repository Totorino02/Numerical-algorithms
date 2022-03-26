"""
    Name: lagrange.py
    Goal: interpolation of newton
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 02/03/2022
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from math import pow
from linearEq.utils.gaussForVal import gauss
from os.path import dirname, join
from interpolation.polynom import Polynom


class MoindreCarre:

    def __init__(self, file, deg):
        self.file = file
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
                Xval = np.arange(-2, 2, 0.1)

                self.polyM2 = self.moindreCarre(2)
                self.polyM3 = self.moindreCarre(3)
                self.polyM4 = self.moindreCarre(4)
                self.polyM5 = self.moindreCarre(5)

                # print the graph
                plt.plot(Xval, self.givenFunc(Xval, "X**2 + 1"), label='Courbe', c='black')
                plt.plot(Xval, self.calc(Xval, self.polyM2), label='Courbe moindreCarre 2')
                plt.plot(Xval, self.calc(Xval, self.polyM3), label='Courbe moindreCarre 3')
                plt.plot(Xval, self.calc(Xval, self.polyM4), label='Courbe moindreCarre 4')
                plt.plot(Xval, self.calc(Xval, self.polyM5), label='Courbe moindreCarre 5')
                plt.scatter(self.X, self.Y, c='red', label='Points Données')
                plt.title("Interpolation de Moindre carré:\nPx1 = {}\nPx2 = {}\nPx3 = {}\nPx4 = {}".format(self.polyM2, self.polyM3, self.polyM4, self.polyM5))
                plt.xlabel("X --->")
                plt.ylabel("Y --->")
                plt.legend()
                plt.show()
        except ValueError:
            print("Valeurs mal définies")
        except TypeError:
            print("None Type n'est pas un type primitif")

    def calc(self, X, poly):
        return eval(poly)

    def givenFunc(self, X, poly):
        return eval(poly)

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
