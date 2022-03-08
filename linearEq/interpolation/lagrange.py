"""
    Name: lagrange.py
    Goal: Numerical resolution of linear equations using the method of jacobi
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 24/02/2022
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from os.path import dirname, join

class Lagrange:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(join(dirname(__file__), self.file))
        X = [float(i) for i in sys.stdin.readline().split()]
        Y = [float(i) for i in sys.stdin.readline().split()]

        if len(X) != len(Y):
            print("Vos tableaux ne sont pas de meme taille")
        else:
            self.X = np.array(X)
            self.Y = np.array(Y)
            self.dim = len(X)
            Xval = np.arange(-10, 10, 0.1)
            Yval = list()
            Y2 = list()
            for i in X:
                Y2.append(self.calc(i))
            for i in Xval:
                Yval.append(self.calc(i))

            plt.plot(Xval, Yval, label='courbe')
            plt.scatter(X, Y2, c='coral', label='Points')
            plt.title("Interpolation de Lagrange")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.show()

    def calc(self, x):
        Px = 0
        for i in range(self.dim):
            fi = 1
            for j in range(self.dim):
                if i != j:
                    fi = fi * (x - self.X[j])/(self.X[i] - self.X[j])
            Px = Px + self.Y[i] * fi
        return Px

