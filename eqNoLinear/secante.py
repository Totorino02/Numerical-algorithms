"""
    Name: bissection.py
    Goal: the numeric resolution with the false postion or secant algorithm :-)
    Author: Dr HOUNSI
    Date: 04/01/2021
"""
import math
from math import pow, fabs

class Secante:
    def __init__(self):
        self.isExist = True; self.List = list()
        self.values()
        self.main()

    def func(self, x):
        """resultat = 0
        for i in range(self.length):
            resultat += (pow(x,(self.length - i-1))*self.list[i])
        return resultat"""

    def calc(self, x):
        #y = math.exp(x)+3*math.sqrt(x)-2
        y = pow(x, 2) - 1
        return y

    def values(self):
        #values = input("Entrez les valeurs de la fonction polynome séparer par des espaces : ")
        #self.list = [float(i) for i in values.split()]
        self.inf = float(input("Borne inf. : "))
        self.sup = float(input("Borne sup. : "))
        self.Dr = float(input("Valeur de l'erreur absolue : "))
        #self.length = len(self.list)

    def main(self):
        X1 = self.inf
        X2 = self.sup
        Xm = X1 - (X2-X1)*(self.calc(X1))/(self.calc(X2)-self.calc(X1))
        print(self.calc(X1), self.calc(Xm), self.calc(X2))
        #if Xm == 0: Xm = self.Dr
        while fabs(X2-X1) >= self.Dr:
            print(X1, Xm, X2)
            if (self.calc(X1) * self.calc(Xm))<0 :
                X2 = Xm ; Xm = X1 - (X2-X1)*(self.calc(X1))/(self.calc(X2)-self.calc(X1))
                #if Xm == 0: Xm = self.Dr
                continue
            elif (self.calc(X2) * self.calc(Xm))<0 :
                X1 = Xm ; Xm = X1 - (X2-X1)*(self.calc(X1))/(self.calc(X2)-self.calc(X1))
                if Xm == 0: Xm = self.Dr
                continue
            else :
                self.isExist = True
                #if Xm == 0: Xm = self.Dr
                break
        #Xm = (X1 + X2) / 2
        if self.isExist :
            print("Resultats:\nX1: {} \nX2 : {} \nXm : {}".format(X1, X2, Xm))
        else:
            print("Pas de solution possible")

calcul = Secante()