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


class MoindreCarre:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(join(dirname(__file__), self.file))
        self.X = [float(i) for i in sys.stdin.readline().split()]
        self.Y = [float(i) for i in sys.stdin.readline().split()]

        if len(self.X) != len(self.Y):
            print("Vos tableaux ne sont pas de meme taille")
        self.dim = len(self.X)
        self.deg = 3  # int(input("Degré de poly.: "))
        matrix = np.zeros((self.deg + 1, self.deg + 1))
        vect = list()
        maxDeg = 2 * self.deg

        # matrix
        for i in range(maxDeg, self.deg - 1, -1):
            for j in range(self.deg + 1):
                temp = [pow(self.X[k], i - j) for k in range(self.dim)]
                matrix[maxDeg - i][j] = sum(temp)

        # vector
        for i in range(self.deg, -1, -1):
            temp = [pow(self.X[k], i) * self.Y[k] for k in range(self.dim)]
            vect.append(sum(temp))

        # polynom coefs
        try:
            self.Coefs = gauss(matrix, vect).showResult()
            print(self.Coefs)
            # print the graph
            Xval = np.arange(-10, 10, 0.1)
            Yval = list()
            for val in Xval:
                Yval.append(self.calc(val))
            plt.plot(Xval, Yval, label='Courbe obtenue', c='black')
            plt.scatter(self.X, self.Y, c='red', label='Points Données')
            plt.title("Interpolation de Moindre carré")
            plt.xlabel("X --->")
            plt.ylabel("Y --->")
            plt.legend()
            plt.show()
        except ValueError:
            print("Valeurs mal définies")
        except TypeError:
            print("None Type n'est pas un type primitif")

    def calc(self, x):
        val = 0
        for i in range(len(self.Coefs)):
            val = val + (self.Coefs[i] * pow(x, i))
        return val
