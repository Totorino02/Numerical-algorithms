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
from interpolation.polynom import Polynom

class Newton:

    def __init__(self, file):
        self.file = file

        try:
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
                        matrix[i][j] = self.calc(j, self.X[i])

                Coefs = gauss(matrix, self.Y).showResult()
                self.poly = Polynom().build(Coefs)

                # polynomes values
                Xval = np.arange(-10, 10, 0.1)
                plt.plot(Xval, self.calcNewton(Xval), label='Courbe obtenue')
                plt.scatter(self.X, self.Y, c='blue', label='Points Données')
                plt.plot(Xval, self.givenFunc(Xval, "X**2 + 1"), label='Courbe', c='red')
                plt.title("Interpolation de Newton\nPx = {}".format(self.poly))
                plt.xlabel("X --->")
                plt.ylabel("Y --->")
                plt.legend()
                plt.show()
        except TypeError:
            print("Erreur lors du calcul veuillez réessayer")
        except ValueError:
            print("Erreur lors de la saisie")

    def calc(self, dim, x):
        val = 1
        for i in range(dim):
            val = val * (x - self.X[i])
        return val

    def calcNewton(self, X):
        return eval(self.poly)

    def givenFunc(self, X, poly):
        return eval(poly)
