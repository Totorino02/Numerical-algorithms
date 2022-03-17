"""
    Name: thomas.py
    Goal: Numerical resolution of linear equations with the method of Thomas
    Author: HOUNSI madouvi antoine-sebastien
    Date: 08/03/2022
"""
from os.path import join, dirname
import sys
import numpy as np
from linearEq.utils.gaussForVal import gauss

class Thomas:

    def __init__(self, file):
        self.file = join(dirname(__file__), file)
        self.dim = self.countLine(self.file)
        self.matrix = list()
        self.vect = list()
        sys.stdin = open(self.file)
        for _ in range(self.dim):
            line = sys.stdin.readline().split("|")
            self.matrix.append([float(x) for x in line[0].split()])
            self.vect.append(float(line[1]))
        if not self.isTridiagonal(self.matrix, self.dim):
            print("Votre matrix n'est pas tridiagonal")
            return
        matL, matU = self.factorization(self.matrix, self.dim)
        # interm = gauss(matL, self.vect).showResult()
        # final = gauss(matU, interm).showResult()
        # print(final)

        sol = self.solution(matL, matU, self.vect, self.dim)
        print(sol)

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

    @staticmethod
    def isTridiagonal(matrix, dim):
        for i in range(dim):
            counter = 0
            for j in range(dim):
                if matrix[i][j] != 0: counter += 1
            if i == 0 and counter > 2: return False
            if counter > 3: return False
        return True

    def factorization(self, matrix, dim):
        matL = np.identity(dim)
        matU = np.zeros([dim, dim])
        matU[0][0] = matrix[0][0]

        for i in range(dim):
            if i != dim-1: matU[i][i+1] = matrix[i][i+1]
            if i > 0:
                matL[i][i-1] = matrix[i][i-1] / matU[i-1][i-1]
                matU[i][i] = matrix[i][i] - matL[i][i-1] * matU[i-1][i]
        """print(matL)
        print()
        print(matU)"""
        return matL, matU

    def solution(self, matL, matU, vect, dim):
        """
            :return: solution
        """
        sY = list()
        sY.append(vect[0])
        for i in range(1, dim):
            s1 = vect[i] - sY[i-1] * matL[i][i-1]
            sY.append(s1)
        # lTM => s
        s = list()
        s.append(sY[dim-1]/matU[dim-1][dim-1])
        for i in range(dim-2, -1, -1):
            try:
                val = (sY[i] - matU[i][i+1] * s[len(s)-1]) / matU[i][i]
                s.append(val)
            except ZeroDivisionError:
                return "Veillez réessayer"
        s = [round(i, 2) for i in s]
        s.reverse()
        return s
