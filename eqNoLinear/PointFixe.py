"""
    Name: PointFixe.py
    Goal: Résolution Numerique des équations non linéaires avec la méthode des points fixes.
    Author: Dr HOUNSI
    Date: 21/12/2021
"""
from math import pow, fabs

class PointFixe:
    """
        Resolution de G(x) = 0  (01)
        soit r la solution de (01); on definit F tel que F(r)=r
        l'agorithme des points fixes:
            - on prend un élément de départ Xo
            - on calcul X1 = F(Xo)
            - on
            - ainsi de suite on a une suite (Xn) / Xn+1 = F(Xn)
            - critère d'arret e
            - si (Xn+1 - Xn)/Xn+1 < e on arret et r=Xn+1
    """
    def __init__(self):
        self.suite()
        #self.InterpolationAitken()

    def function(self):
        """Entrez les valeurs de la fonction: a b c d => aX+bX^2+cX^3+dX^4"""
        """print("Entrez les valeurs de la fonction: a b c d => aX+bX^2+cX^3+dX^4")
        values = input("Coefficients: ")
        self.coefs = [float(i) for i in values.split()]
        self.expo = float(input("expo. : "))"""
        self.inf = float(input("Xo : "))
        self.e = float(input("Erreur absolue (e): "))
        #self.length = len(self.coefs)

    def calc(self, val):
        """calcul de F de val"""
        """result = 0
        for i in range(self.length):
            result += pow(val,(self.length - i-1)) * self.coefs[i]
        result = pow(result, self.expo)
        return result"""
        #y = 1 -val - (pow(val, 2) / 5)
        y = pow(val, 2) - 1
        return y

    def calcDerive(self, val):
        """calcul du derivé de F polynome. si not -1<F(Xo)<1 alors la suite diverge"""
        """list = [j*(self.length - i-1) for (i,j) in enumerate(self.coefs) if i!=self.length-1]
        length = len(list)
        result = 0
        for i in range(length):
            result += pow(val, (length - i - 1)) * list[i]
        result *= pow(self.calc(val), 1-self.expo)
        return result"""
        #resultat = -1 + (-2 / 5) * val
        resultat = 2 * val
        if (resultat == 0):
            resultat += 0.0001
        return resultat

    def suiteStopCondition(self, x, y):
        """condition d'arret de la suite"""
        if (fabs(y - x)) >= self.e:
            return False
        else:
            return True

    def suite(self):
        self.function()
        print(self.calcDerive(self.inf))
        #if -1< self.calcDerive(self.inf) and self.calcDerive(self.inf)<1:
        Xo = self.inf
        X1 = self.calc(Xo)
        #cpt =0;
        while not self.suiteStopCondition(X1, Xo): #and cpt<=50:
            print(Xo, X1)
            print("Valeur de la dérivé: ", self.calcDerive(Xo))
            #cpt+=1
            # on fait le remplacement x0=x1 jusqu'a ce que l'erreur soit minimal
            Xo = X1
            X1 = self.calc(Xo)
        print("\nResultat : ")
        print("X* = ", X1)
        print("En = ", self.calcDerive(X1))
        print("En/En-1 = ", self.calcDerive(X1)/self.calcDerive(Xo))
        print("En/(En-1)^2 = ", self.calcDerive(X1) /pow(self.calcDerive(Xo),2))
        #else: print("la suite (Xn) est divergente")

    def calcInterpolation(self, x, y, z):
        return x -(pow(y-x, 2)/(z-2*y+x))

    def InterpolationAitken(self):
        self.function()
        Xo = self.inf; X1 = self.calc(Xo); X2 = self.calc(X1)
        r = self.calcInterpolation(Xo, X1, X2)
        while fabs(r) > self.e:
            Xo = r
            X1 = self.calc(Xo)
            X2 = self.calc(X1)
            r = self.calcInterpolation(Xo, X1, X2)
        return r

startAlgo = PointFixe()

# e = 0.0000000001