"""
    name: runge-kutta-2.py
    goal: numeric solve of differential equations
    author: Dr HOUNSI Madouvi antoine-sebastien
    date: 28/03/2022
"""

from math import exp, pow
import numpy as np
import matplotlib.pyplot as pt
from interpolation.lagrange import Lagrange


class RungeKutta4:

    def __init__(self):
        self.a = None
        self.b = None
        self.pas = 0.1
        self._getValues()
        result = self._dev(self.a, self.b, self.initial, self.pas)
        vals = np.arange(self.a, self.b+self.pas, self.pas)
        print(len(vals), len(result))
        # print(vals)
        print(Lagrange("runge-kutta-2.py").funcLagrange(vals, result, len(result) - 1))
        # Lagrange("runge-kutta-2.py").showC(vals, result)
        pt.scatter(vals, result, label='Courbe Obtenue')
        # pt.plot(vals, [-pow(x, 2)+x+2 for x in vals], label='Courbe')
        pt.legend()
        pt.show()

    def _getValues(self):
        print("Entrez les valeurs des intervalles [a,b]: ")
        try:
            self.a = float(input("a:"))
            self.b = float(input("b: "))
            if self.a >= self.b:
                print("votre intervalle n'est pas valide")
                self._getValues()
            self.initial = float(input("Valeur initial X0: "))
        except ValueError:
            print("Données incorrecte")
            self._getValues()

    def func(self, X, Y) -> int:
        # return -0.3 * Y + 2 * exp(X)
        # return -2 * X + 1
        return 2*Y - 3*X

    def _dev(self, a, b, X0, pas):
        K1 = 0
        K2 = 0
        K3 = 0
        K4 = 0
        f = X0
        values = list()
        values.append(f)
        val = np.arange(a, b, pas)
        for i in val:
            K1 = self.func(i, f)
            K2 = self.func(i+(pas/2), f+(pas/2)*K1)
            K3 = self.func(i+(pas/2), f+(pas/2)*K2)
            K4 = self.func(i+pas, f + pas*K3)
            f = f + pas/6 * (K1 + 2*K2 + 2*K3 + K4)
            values.append(f)
        return values


RungeKutta4()
