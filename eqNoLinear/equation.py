"""
    name: equation.py
    goal: mettre ensemble tous les algorithmes de résolution
    author: Dr HOUNSI antoine
    date: 26/01/2022
"""

import math
from math import fabs, sqrt, pow
import numpy as np


class Equation:

    def __init__(self):
        self.isExist = True
        self._getValues()

    def _getValues(self):
        try:
            print("\n -******* Résolution des Equations non linéaires *******-\n")
            self.inf = float(input("Borne inf. : "))
            self.sup = float(input("Borne sup. : "))
            if self.inf >= self.sup:
                print("\nvotre intervalle n'est pas valide")
                self._getValues()
            # self.Dr = float(input("Valeur de l'erreur absolue : "))
            self.Dr = 0.0000000001
            self.Xe = float(input("Xo : "))
            self.nMax = 10000
        except ValueError:
            print("\nDonnées incorrectes")
            self._getValues()

        self.bissection()
        self.secante()
        self.newton()
        self.pntsFixes()
        self._getValues()

    def calc(self, x):
        # y = (pow(x, 2) - 4) / (x - 1)
        # y = 2 * pow(x, 3) - 7 * pow(x, 2) + 8 * x
        y = x ** 2 - 2 * x
        return y

    def derive(self, x):
        # resultat = (pow(x, 2) - 2 * x + 4) / (pow(x, 2) - 2 * x + 1)
        # resultat = 6 * pow(x, 2) - 14 * x + 8
        resultat = 2 * x - 2
        return resultat

    def calcptf(self, x):
        y = x - 3 + (x + 1) / (x - 1)
        return y

    def deriveptf(self, x):
        resultat = 1 - 2 / pow(x - 1, 2)
        return resultat

    def suiteStopCondition(self, x, y):
        """condition d'arret de la suite"""
        if (fabs(y - x)) >= self.Dr:
            return False
        else:
            return True

    def bissec(self, X1, X2):
        Xm = (X1 + X2) / 2
        while fabs((X2 - X1) / 2) >= self.Dr:
            if (self.calc(X1) * self.calc(Xm)) < 0:
                X2 = Xm
                Xm = (X1 + X2) / 2
                continue
            elif (self.calc(X2) * self.calc(Xm)) < 0:
                X1 = Xm
                Xm = (X1 + X2) / 2
                continue
        return Xm

    def balayage(self, a, b):
        tab = np.arange(a, b, 0.1)
        result = list()
        for i in range(1, len(tab)):
            if self.calc(tab[i - 1]) * self.calc(tab[i]) < 0:
                result.append(self.bissec(tab[i - 1], tab[i]))
        return result

    def bissection(self):
        X1 = self.inf
        X2 = self.sup
        # catch zero division error & Traitement trop long
        try:
            if (self.calc(X1) * self.calc(X2)) > 0:
                Xm = self.balayage(X1, X2)
            else:
                Xm = (self.inf + self.sup) / 2
                while fabs((X2 - X1) / 2) >= self.Dr:
                    # print(X1, Xm, X2)
                    if self.calc(X1) == 0:
                        Xm = X1
                    elif self.calc(X2) == 0:
                        Xm = X2
                    elif (self.calc(X1) * self.calc(Xm)) < 0:
                        X2 = Xm
                        Xm = (X1 + X2) / 2
                        continue
                    elif (self.calc(X2) * self.calc(Xm)) < 0:
                        X1 = Xm
                        Xm = (X1 + X2) / 2
                        continue
                    else:
                        # self.isExist = True
                        # if Xm == 0: Xm = self.Dr
                        Xm = self.balayage(X1, X2)
                        break
            print("Resultats Dichotomie: Xm = {0}".format(Xm))
        except ZeroDivisionError:
            print("Dichotomie: => Erreur division par zéro")
        except TimeoutError:
            print("Dichotomie: => Traitement trop long")
        except OverflowError:
            print("Dichotomie: => Overflow error")
        except ValueError:
            print("Dichotomie: => Vous etes sortie du domaine de définition")

    def secante(self):
        X1 = self.inf
        X2 = self.sup
        cpt = 0
        try:
            """if (self.calc(X1) * self.calc(X2)) > 0:
                print("Bissection: Pas de solution ou interval non rafiné")
                return None"""
            Xm = X1 - (X2 - X1) * (self.calc(X1)) / (self.calc(X2) - self.calc(X1))

            while fabs(X2 - X1) >= self.Dr and cpt < self.nMax:

                cpt += 1
                # if (self.calc(X1) * self.calc(Xm)) < 0:
                if Xm > X2:
                    X1 = X2
                    X2 = Xm
                    Xm = X1 - (X2 - X1) * (self.calc(X1)) / (self.calc(X2) - self.calc(X1))
                    continue
                elif Xm < X2:
                    X1 = X2
                    X2 = Xm
                    Xm = X1 - (X2 - X1) * (self.calc(X1)) / (self.calc(X2) - self.calc(X1))
                    # if Xm == 0: Xm = self.Dr
                    continue
                else:
                    self.isExist = False
                    break
            if self.isExist:
                print("Resultats Sécante: Xm = {0}".format(Xm))
            else:
                print("Pas de solution possible")
        except ZeroDivisionError:
            print("Secante: => division par zéro")
        except TimeoutError:
            print("Secante: => Traitement trop long")
        except OverflowError:
            print("Secante: => Overflow error")
        except ValueError:
            print("Dichotomie: => Vous etes sortie du domaine de définition")

    def newton(self):
        X1 = self.Xe
        try:
            Xm = X1 - (self.calc(X1) / self.derive(X1))
            while fabs(Xm - X1) >= self.Dr:
                X1 = Xm
                Xm = X1 - self.calc(X1) / self.derive(X1)
                continue
            if self.isExist:
                print("Resultat Newton: Xm = {} ".format(Xm))
            else:
                print("Pas de solution possible")
        except ZeroDivisionError:
            print("Newton: => Division par zéro")
        except TimeoutError:
            print("Newton: => Traitement trop long")
        except OverflowError:
            print("Newton: => Overflow error")
        except ValueError:
            print("Dichotomie: => Vous etes sortie du domaine de définition")

    def pntsFixes(self):
        Xo = self.Xe
        try:
            X1 = self.calcptf(Xo)
            if abs(self.deriveptf(Xo)) > 1:
                print("Points Fixes: => Fonction divergente")
                return None
            cpt = 0
            while not self.suiteStopCondition(X1, Xo) and cpt < 10:
                cpt += 1
                Xo = X1
                X1 = self.calcptf(Xo)
                print(self.deriveptf(X1))
            print("Resultat Points Fixes: Xm = {} ".format(X1))
        except ZeroDivisionError:
            print("Points Fixes: => Division par zéro")
        except TimeoutError:
            print("Points Fixes: => Traitement trop long")
        except OverflowError:
            print("Points Fixes: => Fonction divergente")
        except ValueError:
            print("Dichotomie: => Vous etes sortie du domaine de définition")


Equation()
