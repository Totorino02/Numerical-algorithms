"""
    Name: choleski.py
    Goal: Numerical resolution of linear equations with the method of choleski
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 16/02/2022
"""
import sys
from math import pow
from os.path import dirname, join


class Choleski:

    def __init__(self, file):
        self.file = file

    def _getValues(self, file):
        sys.stdin = open(join(dirname(__file__), file))
        self.dim = self.countLine(file)
        self.matrix = list()
        self.matrixL = list()
        self.matrixU = list()
        self.vect = list()
        self.result = list()
        try:
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([float(i) for i in line[0].split()])
                self.matrixU.append([0 for i in range(self.dim)])
                self.matrixL.append([0 for i in range(self.dim)])
                self.vect.append(float(line[1]))
        except TypeError:
            print("type error")

    def isSymetric(self):
        self.counter = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.matrix[i][j] != self.matrix[j][i]:
                    self.counter += 1
        if self.counter == 0:
            return True
        else:
            return False

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

    def triangularize(self):
        self.matrixL[0][0] = pow(self.matrix[0][0], 0.5)
        for i in range(1, self.dim, 1):
            self.matrixL[i][0] = self.matrix[i][0] / self.matrixL[0][0]
        for i in range(1, self.dim, 1):
            for j in range(i, self.dim):
                sum = 0
                if i == j:
                    for k in range(j):
                        sum += pow(self.matrixL[j][k], 2)
                    self.matrixL[j][i] = pow(self.matrix[j][i] - sum, 0.5)
                else:
                    for k in range(j):
                        sum += self.matrixL[j][k] * self.matrixL[k][i]
                    self.matrixL[j][i] = (self.matrix[j][i] - sum) / self.matrixL[i][i]
        for i in range(self.dim):
            for j in range(self.dim):
                self.matrixU[i][j] = self.matrixL[j][i]

    def solution(self):
        """
            :return: solution
        """
        # uTM => sY
        try:
            self._getValues(self.file)
            sY = list()
            if self.isSymetric():
                try:
                    self.triangularize()
                except ZeroDivisionError:
                    return "La matrice est mal d??finie"
                except ValueError:
                    return "La matrice est mal d??finie"
            else:
                return "La Matrice n'est pas symetrique"
            sY.append(self.vect[0] / self.matrixL[0][0])
            for i in range(1, self.dim):
                s1 = 0
                for k in range(i):
                    temp = self.matrixL[i][k] * sY[k]
                    s1 += temp
                val = (self.vect[i] - s1) / self.matrixL[i][i]
                sY.append(val)
            # lTM => s
            s = list()
            s.append(sY[self.dim - 1] / self.matrixU[self.dim - 1][self.dim - 1])
            for i in range(self.dim - 2, -1, -1):
                s1 = 0
                for k in range(self.dim - 1, i, -1):
                    temp = self.matrixU[i][k] * s[self.dim - k - 1]
                    s1 += temp
                val = (sY[i] - s1) / self.matrixU[i][i]
                s.append(val)
            s = [round(i, 2) for i in s]
            s.reverse()
            return s
        except ZeroDivisionError:
            return "division per z??ro"
        except RuntimeError:
            return "Erreur lors de l'execution"
        except TypeError:
            return "Donn??es non variables"
        except IndexError:
            return "Erreur lors de l'indexation"
        except EOFError:
            return "Eof error"
        except ValueError:
            return "Erreur lors de la saisie"



    def showMatrixL(self):
        """
            :return:
        """
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(self.matrixL[_][i]), end="")  # the 7.2f is arbitrary
            print("\n")

    def showMatrixU(self):
        """
            :return:
        """
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(self.matrixU[_][i]), end="")  # the 7.2f is arbitrary
            print("\n")


"""
    problems : 
        line 62 self.matrix[j][i] - sum < 0  : math error
"""
