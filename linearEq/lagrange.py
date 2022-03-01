"""
    Name: lagrange.py
    Goal: Numerical resolution of linear equations using the method of jacobi
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 24/02/2022
"""
import numpy as np
import matplotlib.pyplot as plt

class lagrange:

    def __init__(self):
        print("\t\t\t-------------------------------------")
        print("\t\t\t|\tInterpolation de LAGRANGE        |")
        print("\t\t\t-------------------------------------")

        Xin = input("X: ")
        Yin = input("Y: ")
        X = [float(i) for i in Xin.split()]
        Y = [float(i) for i in Yin.split()]

        if len(X) != len(Y):
            print("Vos tableaux ne sont pas de meme taille")
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.dim = len(X)
        Xval = np.arange(-5,5,0.1)
        Yval = list()
        Y2 = list()
        for i in X:
            Y2.append(self.calc(i))
        for i in Xval:
            Yval.append(self.calc(i))

        plt.plot(Xval, Yval)
        plt.scatter(X, Y2)
        plt.title("Interpolation de Lagrange")
        plt.xlabel("X")
        plt.ylabel("Y")
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
#-2 -1 0 1 2
#5 2 1 2 5

#-2 0 1 2
#4 0 0 4
la = lagrange()