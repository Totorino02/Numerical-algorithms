"""
    Name: choleski.py
    Goal: Numerical resolution of linear equations with the method of choleski
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 16/02/2022
"""
import math
import sys
from math import pow

class choleski:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(self.file)
        self.dim = self.countLine(file)
        self.matrix = list()
        self.matrixL = list()
        self.matrixU = list()
        self.vect = list()
        self.result = list()
        try:
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([(float)(i) for i in line[0].split()])
                self.matrixU.append([0 for i in range(self.dim)])
                self.matrixL.append([0 for i in range(self.dim)])
                self.vect.append(float(line[1]))

            # add of the vector to the matrix
            """for i in range(self.dim):
                self.matrix[i].append(self.vect[i])"""
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

    def triangularize(self):

        self.matrixL[0][0] = pow(self.matrix[0][0], 0.5)
        for i in range(1,self.dim,1):
            self.matrixL[i][0] = self.matrix[i][0]/self.matrixL[0][0]

        for i in range(1,self.dim,1):
            for j in range(i, self.dim):
                sum = 0
                if i == j:
                    for k in range(j):
                        sum += pow(self.matrix[i][j],2)
                    self.matrixL[j][i] = pow(self.matrix[j][i] - sum, 0.5)
                else:
                    for k in range(j):
                        sum += self.matrixL[j][k]*self.matrixL[i][k]
                    self.matrixL[j][i] = (self.matrix[j][i] - sum)/self.matrix[i][i]

        for i in range(self.dim):
            for j in range(self.dim):
                self.matrixU[i][j] = self.matrixL[j][i]

        print(self.matrixL)
        print(self.matrixU)

    def solution(self):
        """
            :return: solution
        """
        #uTM => sY
        sY = list()
        sY.append(self.vect[0]/self.matrixL[0][0])
        for i in range(1, self.dim):
            s1 = 0
            for k in range(i):
                temp = self.matrixL[i][k]*sY[k]
                s1 += temp
            val = (self.vect[i] - s1)/self.matrixL[i][i]
            sY.append(val)
        #lTM => s
        s = list()
        s.append(sY[self.dim-1])
        for i in range(self.dim-2, -1, -1):
            s1 = 0
            for k in range(self.dim-1,i,-1):
                temp = self.matrixU[i][k] * s[self.dim-k-1]
                s1 += temp
            val = (sY[i] - s1) / self.matrixU[i][i]
            s.append(val)
        s = [round(i,2) for i in s]
        s.reverse()
        return s

"""
    problems : 
        line 62 self.matrix[j][i] - sum < 0  : math error
"""