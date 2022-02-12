"""
    Name: LU.py
    Goal: Numerical resolution of linear equations with decomposition of Crout
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 02/02/2022
"""
import sys

class LU:

    def __init__(self, file):
        sys.stdin = open(file)
        self.len = self.countLine(file)
        self.matrix = list()
        self.matrixL = list()
        self.matrixU = list()
        self.vect = list()
        for _ in range(self.len):
            line = sys.stdin.readline().split("|")
            self.matrix.append([(float)(i) for i in line[0].split()])
            self.matrixU.append([0 for i in range(self.len)])
            self.matrixL.append([0 for i in range(self.len)])
            self.vect.append(float(line[1]))
        self.triangularize()

    def countLine(self,file):
        """
            :param file:
            :return: nbOfLine
        """
        cpt = 0
        with open(file) as f:
            for line in f:
                if not line.isspace():
                    cpt+=1
        return cpt

    def triangularize(self):
        """
            in this section the target is triangularize the inital matrix and have
            upper and lower triangular matrix
                    for i in range(1, n)
                        for j in range(1, i)
                             i values in line i and column i
            :return: matrixL, matrixU
        """
        #base values
        for i in range(self.len):
            self.matrixL[i][0] = round(self.matrix[i][0], 2)
            self.matrixU[0][i] = round((self.matrix[0][i]) / (self.matrixL[0][0]), 2)
        for i in range(self.len):
            self.matrixU[i][i] = 1
        #
        for i in range(1, self.len):
            for j in range(i, self.len):
                S1 = 0; S2 = 0
                for k in range(i):
                    S1 += self.matrixL[j][k]*self.matrixU[k][i]
                    S2 += self.matrixL[i][k] * self.matrixU[k][j];
                self.matrixL[j][i] = self.matrix[j][i] - S1
                self.matrixU[i][j] = (self.matrix[i][j] - S2)/self.matrixL[i][i]

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
        #uTM => sY
        sY = list()
        sY.append(self.vect[0]/self.matrixL[0][0])
        for i in range(1, self.len):
            s1 = 0
            for k in range(i):
                temp = self.matrixL[i][k]*sY[k]
                s1 += temp
            val = (self.vect[i] - s1)/self.matrixL[i][i]
            sY.append(val)
        #lTM => s
        s = list()
        s.append(sY[self.len-1])
        for i in range(self.len-2, -1, -1):
            s1 = 0
            for k in range(self.len-1,i,-1):
                temp = self.matrixU[i][k] * s[self.len-k-1]
                s1 += temp
            val = (sY[i] - s1) / self.matrixU[i][i]
            s.append(val)
        return s

