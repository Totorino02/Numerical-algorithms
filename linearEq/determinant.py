"""
    Name: choleski.py
    Goal: Numerical resolution of linear equations with the method of choleski
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 16/02/2022
"""
import sys

class determinant:

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