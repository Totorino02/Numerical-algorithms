import math
from typing import List


class Polynome(list):
    """La classe Polynome va nous permettre de bien manipuler des objets de type polynome
    à coefficient floattant.
    """

    def __init__(self, lstCoef: List[float]) -> None:
        super().__init__(lstCoef)
        self.coefs = lstCoef  # Pas obligé
        self.degree = len(lstCoef) - 1

    def __init__(self, n: int, el: int) -> None:
        super().__init__([el] * (n + 1))
        self.degree = n

    def __repr__(self) -> str:
        represent = "\n("
        # represent += ", ".join([str(coef) for coef in self.coefs])
        represent += ", ".join([str(coef) for coef in self])
        represent = represent + ")\n"

        return represent

    def __str__(self) -> str:

        represent = "\n("
        # represent += ", ".join([str(coef) for coef in self.coefs])
        represent += ", ".join([str(coef) for coef in self])
        represent = represent + ")\n"

        return represent

    def __getitem__(self, index):
        if (index > self.degree): return 0
        return super().__getitem__(index)

    def __add__(self, P):
        return sumPolynome(self, P)

    def __iadd__(self, P):
        return self.__add__(P)

    def __neg__(self):
        return mulByScalar(self, -1)

    def __sub__(self, P):
        return subPolynome(self, P)

    def __isub__(self, P):
        return self.__sub__(P)

    def __rmul__(self, scalar):
        return mulByScalar(self, scalar)

    def __mul__(self, P):
        return ProductPolynome(self, P)

    def __imul__(self, P):
        return self.__mul__(P)

    def derivate(self, ordre: int = 1):
        if (ordre == 0): return self
        if (ordre == self.degree): return Polynome(0, self[ordre] * math.factorial(ordre))
        if (ordre > self.degree): return Polynome(0, 0)

        dP = Polynome(self.degree - ordre, 0)
        if (ordre == 1):
            for i in range(self.degree):
                dP[i] = (i + 1) * self[i + 1]
            return dP

        return self.derivate(ordre - 1).derivate()

    def primitive(self):

        pass


def sumPolynome(A: Polynome, B: Polynome) -> Polynome:
    return Polynome([A[i] + B[i] for i in range(len(A))])


def subPolynome(A: Polynome, B: Polynome) -> Polynome:
    return Polynome([A[i] - B[i] for i in range(len(A))])


def mulByScalar(A: Polynome, scalar: float) -> Polynome:
    return Polynome([scalar * el for el in A])


def ProductPolynome(A: Polynome, B: Polynome) -> Polynome:
    P = Polynome(A.degree + B.degree, 0)
    n = P.degree
    for i in range(n + 1):
        for j in range(i + 1):
            P[i] += A[j] * B[i - j]

    return P

