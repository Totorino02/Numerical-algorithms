"""
    Name: newton.py
    Goal: the numeric resolution with newton algorithm :-)
    Author: Dr HOUNSI
    Date: 04/01/2021
"""
import math
from math import pow, fabs

class Newton:
    def __init__(self):
        self.isExist = True; self.List = list()
        self.values()
        self.main()

    def func(self, x):
        resultat = 0
        for i in range(self.length):
            resultat += (pow(x,(self.length - i-1))*self.list[i])
        return resultat

    def calc(self, x):
        #y = 1 - x -(pow(x,2)/5)
        y = pow(x,2)-1
        return y

    def derive(self, x):
        #resultat = (-2/5)*x-1
        resultat = 2*x
        if(resultat == 0):
            resultat+=0.0001
        return resultat

    def values(self):
        self.inf = float(input("Entrez la valeur. : "))
        self.Dr = float(input("Valeur de l'erreur absolue : "))

    def main(self):
        X1 = self.inf
        Xm = X1 - (self.calc(X1)/self.derive(X1))
        print(self.calc(X1), self.calc(Xm))
        while fabs(Xm-X1) >= self.Dr:
            print(X1, Xm)
            X1 = Xm
            Xm = X1 - self.calc(X1)/self.derive(X1)
            continue
        if self.isExist :
            print("Resultats:\nX1: {} \nXm : {}".format(X1, Xm))
        else:
            print("Pas de solution possible")

calcul = Newton()

# 0.8541019662496845 => Newton
# 0.8541019660377508 => PointFixe
# 0.000000001