"""
    Name: jacobi.py
    Goal: Numerical resolution of linear equations using the method of jacobi
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 19/02/2022
"""
import sys
from math import pow
from os.path import dirname, join

class jacobi:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(join(dirname(__file__), self.file))
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
        if (val1/val2) <= self.e:
            return True
        else: return False

    def solution(self):
        solution = [0 for i in range(self.dim)]
        cpt = 0
        try:
            while not self.test(self.initialVal) and cpt < 200:
                cpt +=1
                for i in range(self.dim):
                    sum = 0
                    for j in range(self.dim):
                        if j != i:
                            sum += self.matrix[i][j]*self.initialVal[j]
                    try:
                        Xi = (1 / self.matrix[i][i]) * (self.vect[i] - sum)
                    except ZeroDivisionError:
                        return "Veuillez Réesayez Probleme d'optimisation systeme"
                    solution[i] = Xi
                self.initialVal = [i for i in solution]
        except OverflowError:
            return "JACOBI :=> Depassement de capacité réessayer avec d'autes valeurs initiales"
        except IndexError:
            return "Erreur lors de la saisie"
        return self.initialVal
