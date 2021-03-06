"""
    Name: gaussSeidel.py
    Goal: Numerical resolution of linear equations using the method of gauss-seidel
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 23/02/2022
"""
import sys
from math import pow
from os.path import dirname, join


class gaussSeidel:

    def __init__(self, file):
        self.file = file

    def _getValues(self, file):
        sys.stdin = open(join(dirname(__file__), file))
        self.dim = self.countLine(self.file)
        self.matrix = list()
        self.vect = list()
        self.e = 0.001
        self.initialVal = list()
        for _ in range(self.dim):
            """Read data from the file"""
            line = sys.stdin.readline().split("|")
            self.matrix.append([float(i) for i in line[0].split()])
            self.vect.append(float(line[1]))
            self.initialVal.append(float(line[2]))
        #
        for i in range(self.dim):
            self.matrix[i].append(self.vect[i])

        # if a value in a diagonal is null, inverse the line with another line
        for i in range(self.dim):
            while self.matrix[i][i] == 0:
                # inversion if the begin of the pivot is null: L_i <-> L_maxVal
                tempCtab = self.matrix[i][i]
                maxValIndex = i
                for cpt in range(i, self.dim):
                    if abs(self.matrix[cpt][i]) > tempCtab:
                        maxValIndex = cpt
                temporalTab = [x for x in self.matrix[i]]
                self.matrix[i] = [x for x in self.matrix[maxValIndex]]
                self.matrix[maxValIndex] = [x for x in temporalTab]
        #
        for i in range(self.dim):
            self.vect[i] = self.matrix[i][self.dim]
            self.matrix[i].pop(self.dim)

    def countLine(self, file):
        """
            :param file:
            :return: nbOfLine
        """
        cpt = 0
        with open(join(dirname(__file__), self.file)) as f:
            for line in f:
                if not line.isspace():
                    cpt += 1
        return cpt

    def test(self, tab):
        result = list()
        for i in range(self.dim):
            summ = 0
            for j in range(self.dim):
                summ += self.matrix[i][j] * tab[j]
            result.append(summ - self.vect[i])

        interm = [pow(i, 2) for i in result]
        # print(interm)
        val1 = pow(sum(interm), 0.5)
        # print(val1)
        interm = [pow(i, 2) for i in self.vect]
        val2 = pow(sum(interm), 0.5)
        if (val1 / val2) <= self.e:
            return True
        else:
            return False

    def solution(self):
        cpt = 0
        try:
            self._getValues(self.file)
            while not self.test(self.initialVal) and cpt < 350:
                cpt += 1
                for i in range(self.dim):
                    sum = 0
                    for j in range(self.dim):
                        if j != i:
                            sum += self.matrix[i][j] * self.initialVal[j]
                    try:
                        Xi = (1 / self.matrix[i][i]) * (self.vect[i] - sum)
                    except ZeroDivisionError:
                        return "Veuillez R??esayez Probleme d'optimisation systeme"
                    self.initialVal[i] = Xi # round(Xi,6)
        except OverflowError:
            return "GAUSS-SEIDEL :=> Depassement de capacit?? r??essayer avec d'autes valeurs initiales"
        return self.initialVal
