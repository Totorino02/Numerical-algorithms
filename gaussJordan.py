"""
    Name: gaussJordan.py
    Goal: Numerical resolution of linear equations with the method of Gauss Jordan
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 03/02/2022
"""
import sys
from gauss import gauss
from math import ceil


class gaussJordan:
    def __init__(self, file):
        self.file = file
        sys.stdin = open(self.file)
        self.dim = self.countLine(file)
        self.matrix = list()
        self.vect = list()
        self.result = list()
        self.matrixT1 = list()
        try:
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([(float)(i) for i in line[0].split()])
                self.vect.append(float(line[1]))
                # add of the vector to the matrix
            for i in range(self.dim):
                self.matrix[i].append(self.vect[i])
        except TypeError:
            print("type error")

    def countLine(self, file):
        """
            :param file:
            :return: nbOfLine
        """
        cpt = 0
        with open(file) as f:
            for line in f:
                if not line.isspace():
                    cpt += 1
        return cpt

    def showResult(self):
        self.matrixT1 = gauss(self.file).triangularize()
        # print(self.matrixT1)
        for i in range(self.dim):
            coef = self.matrixT1[i][i]
            self.matrixT1[i] = [(1/coef)*i for i in self.matrixT1[i]]

        for i in range(self.dim-1, -1,-1):
            for j in range(i-1, -1,-1):
                coef = self.matrixT1[j][i]
                for k in range(self.dim + 1):
                    self.matrixT1[j][k] = (self.matrixT1[j][k] -coef* self.matrixT1[i][k])

        # print(self.matrixT1)
        for i in range(self.dim):
            self.result.append(round(self.matrixT1[i][self.dim],2))
        self.result.reverse()
        print(self.result)

