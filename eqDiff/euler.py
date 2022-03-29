"""
    name: euler.py
    goal: numeric solve of differential equations
    author: Dr HOUNSI Madouvi antoine-sebastien
    date: 28/03/2022
"""

from math import exp, pow
import numpy as np
import matplotlib.pyplot as pt
from interpolation.lagrange import Lagrange


class Euler:
    def __init__(self):
        self.a = None
        self.b = None
        self.pas = 0.1
        self._getValues()
        result = self._dev(self.a, self.b, self.initial, self.pas)
        vals = np.arange(self.a, self.b + self.pas, self.pas)
        print(len(vals), len(result))
        # print(vals)
        print(Lagrange("runge-kutta.py").funcLagrange(vals, result, len(result) - 1))
        # Lagrange("runge-kutta.py").showC(vals, result)
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
        return -2 * X + 1

    def _dev(self, a, b, X0, pas):
        f = X0
        values = list()
        values.append(f)
        val = np.arange(a, b, pas)
        for i in val:
            f = values[-1] + pas * self.func(i, f)
            values.append(f)
        return values


Euler()
