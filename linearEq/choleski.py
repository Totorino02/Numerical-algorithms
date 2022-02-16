"""
    Name: choleski.py
    Goal: Numerical resolution of linear equations with the method of choleski
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 16/02/2022
"""

import sys
from gauss import gauss

class choleski:

    def __init__(self, file):
        self.file = file
        sys.stdin = open(self.file)
        self.dim = self.countLine(file)
        self.matrix = list()
        self.vect = list()
        self.result = list()
        self.matrixIn = list()
        self.matrixId = list()
        try:
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([(float)(i) for i in line[0].split()])
                self.vect.append(float(line[1]))
                # add of the vector to the matrix
            for i in range(self.dim):
                self.matrix[i].append(self.vect[i])
                self.matrixId.append([0 for i in range(self.dim)])
                self.matrixIn.append([])
            for j in range(self.dim):
                for k in range(self.dim):
                    if k == j:
                        self.matrixId[j][k] = 1
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

    def inverse(self):

        # upper triangular matrix from the gauss class
        for i in range(self.dim):
            self.matrix[i].pop(self.dim);
            for j in range(self.dim):
                self.matrix[i].append(self.matrixId[i][j])

        #
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                cpt = i
                while self.matrix[i][i] == 0 and cpt < self.dim:
                    # inversion if the begin of the pivot is null: L_i <-> L_cpt
                    temporalTab = [x for x in self.matrix[i]]
                    self.matrix[i] = [x for x in self.matrix[cpt + 1]]
                    self.matrix[cpt + 1] = [x for x in temporalTab]
                    cpt += 1
                if self.matrix[j][i] != 0:
                    fMultiplicatif = -(self.matrix[i][i] / self.matrix[j][i])
                    self.matrix[j] = [(fMultiplicatif * x) for x in self.matrix[j]]
                    # last step of the modification the value
                    for k in range(i, self.dim + 1):
                        self.matrix[j][k] = (self.matrix[i][k] + self.matrix[j][k])

        # modification of the matrix to the the diagonal values to 1
        for i in range(self.dim):
            coef = self.matrix[i][i]
            self.matrix[i] = [(1 / coef) * i for i in self.matrix[i]]
        # print(self.matrixT1)
        print(self.matrix)

        # last step output diagonal matrix of 1
        for i in range(self.dim-1, -1,-1):
            for j in range(i-1, -1,-1):
                coef = self.matrix[j][i]
                for k in range(self.dim*2):
                    self.matrix[j][k] = (self.matrix[j][k] -coef* self.matrix[i][k])
        print(self.matrix)

        # isolement de la matrice inversée
        for i in range(self.dim):
            for j in range(self.dim, self.dim*2,1):
                self.matrixIn[i].append(self.matrix[i][j])
        print("\n\n",self.matrixIn)