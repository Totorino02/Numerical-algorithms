"""
    Name: LU.py
    Goal: Numerical resolution of linear equations with decomposition of Crout
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 02/02/2022
"""
import sys
from os.path import dirname, join

class Doulit:

    def __init__(self, file):
        self.file = join(dirname(__file__), file)
        self.len = self.countLine()
        sys.stdin = open(self.file)
        self.matrix = list()
        self.matrixL = list()
        self.matrixU = list()
        self.vect = list()

        #Read data from the file
        for _ in range(self.len):
            line = sys.stdin.readline().split("|")
            self.matrix.append([(float)(i) for i in line[0].split()])
            self.matrixU.append([0 for i in range(self.len)])
            self.matrixL.append([0 for i in range(self.len)])
            self.vect.append(float(line[1]))

    def countLine(self):
        """
            :return: nbOfLine
        """
        cpt = 0
        with open(self.file) as f:
            for line in f:
                if not line.isspace():
                    cpt+=1
        return cpt

    def inversion(self, i, mat, all=False):
        tempCtab = mat[i][i]
        maxValIndex = i
        for cpt in range(i, self.len):
            if abs(mat[cpt][i]) > tempCtab:
                maxValIndex = cpt
        temporalTab = [x for x in mat[i]]

        mat[i] = [x for x in mat[maxValIndex]]
        mat[maxValIndex] = [x for x in temporalTab]

        vectTemp = self.vect[i]
        self.vect[i] = self.vect[maxValIndex]
        self.vect[maxValIndex] = vectTemp

        if all:
            tempM = [x for x in self.matrix[i]]
            self.matrix[i] = [x for x in self.matrix[maxValIndex]]
            self.matrix[maxValIndex] = [x for x in tempM]

    def triangularize(self):
        """
            in this section the target is triangularize the inital matrix and have
            upper and lower triangular matrix
                    for i in range(1, n)
                        for j in range(1, i)
                             i values in line i and column i
            :return: matrixL, matrixU
        """

        # base values

        self.inversion(0, self.matrix)
        for i in range(self.len):
            self.matrixL[i][0] = round(self.matrix[i][0], 2)
            self.matrixU[0][i] = round((self.matrix[0][i]) / (self.matrixL[0][0]), 2)
        for i in range(self.len):
            self.matrixU[i][i] = 1

        # triangularize the matrix
        for i in range(1, self.len):
            for q in range(i, self.len):
                S1 = 0
                for k in range(i):
                    S1 += self.matrixL[q][k] * self.matrixU[k][i]
                self.matrixL[q][i] = self.matrix[q][i] - S1
            if self.matrixL[i][i] == 0:
                self.inversion(i, self.matrixL, True)
            for j in range(i+1, self.len):
                S2 = 0
                for k in range(i):
                    S2 += self.matrixL[i][k] * self.matrixU[k][j]
                    # print("Multi:  ", i, self.matrixL[i][k], " * ", self.matrixU[k][j])
                self.matrixU[i][j] = (self.matrix[i][j] - S2)/self.matrixL[i][i]
                # print("MatU val:", self.matrix[i][j], S2, self.matrixL[i][i], self.matrixU[i][j])

        return self.matrixL, self.matrixU

    def showMatrixL(self):
        """
            :return:
        """
        for _ in range(self.len):
            for i in range(self.len):
                print('{:7.2f}'.format(self.matrixL[_][i]), end="") # the 7.2f is arbitrary
            print("\n")

    def showMatrixU(self):
        """
            :return:
        """
        for _ in range(self.len):
            for i in range(self.len):
                print('{:7.2f}'.format(self.matrixU[_][i]), end="") # the 7.2f is arbitrary
            print("\n")

    def solution(self):
        """
            :return: solution
        """
        self.triangularize()
        sY = list()
        sY.append(self.vect[0]/self.matrixL[0][0])
        for i in range(1, self.len):
            s1 = 0
            for k in range(i):
                temp = self.matrixL[i][k]*sY[k]
                s1 += temp
            val = (self.vect[i] - s1)/self.matrixL[i][i]
            sY.append(val)
        # lTM => s
        s = list()
        s.append(sY[self.len-1])
        for i in range(self.len-2, -1, -1):
            s1 = 0
            for k in range(self.len-1,i,-1):
                temp = self.matrixU[i][k] * s[self.len-k-1]
                s1 += temp
            try:
                val = (sY[i] - s1) / self.matrixU[i][i]
            except ZeroDivisionError:
                return "Veillez réesayer"
            s.append(val)
        s = [round(i, 2) for i in s]
        s.reverse()
        return s
