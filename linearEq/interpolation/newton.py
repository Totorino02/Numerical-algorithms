"""
    Name: lagrange.py
    Goal: interpolation of newton
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 02/03/2022
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from linearEq.utils.gaussForVal import gauss
from os.path import dirname, join

class Newton:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(join(dirname(__file__), self.file))
        self.X = [float(i) for i in sys.stdin.readline().split()]
        self.Y = [float(i) for i in sys.stdin.readline().split()]

        if len(self.X) != len(self.Y):
            print("Vos tableaux ne sont pas de meme taille")
        else:
            self.dim = len(self.X)

            matrix = np.zeros((self.dim, self.dim))
            for i in range(self.dim):
                for j in range(i+1):
                    matrix[i][j] = self.calc(j,self.X[i])
            Coefs = gauss(matrix, self.Y).showResult()

            # polynomes values
            Xval = np.arange(-10, 10, 0.1)
            Yval = list()
            try:
                for val in Xval:
                    Px = 0
                    for j in range(self.dim):
                        Px = Px + Coefs[j] * self.calc(j, val)
                    Yval.append(Px)
                plt.plot(Xval, Yval, label='Courbe obtenue', c='red')
                plt.scatter(self.X, self.Y, c='blue', label='Points Données')
                plt.title("Interpolation de Newton")
                plt.xlabel("X --->")
                plt.ylabel("Y --->")
                plt.legend()
                plt.show()
            except TypeError:
                print("Erreur lors du calcul veuillez réessayer")

    def calc(self, dim, x):
        val = 1
        for i in range(dim):
            val = val * (x - self.X[i])
        return val
