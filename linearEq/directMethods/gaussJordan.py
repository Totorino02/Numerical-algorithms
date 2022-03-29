"""
    Name: gaussJordan.py
    Goal: Numerical resolution of linear equations with the method of Gauss Jordan
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 03/02/2022
"""
import sys
from linearEq.directMethods.gauss import Gauss
from os.path import dirname, join


class GaussJordan:
    def __init__(self, file):
        self.vect = None
        self.matrix = None
        self.file = join(dirname(__file__), file)
        self.dim = self.countLine(self.file)

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

    def getData(self, file):
        """
            get the data from file
            :param file:
        """
        self.matrix = list()
        self.vect = list()
        sys.stdin = open(file)
        for _ in range(self.dim):
            line = sys.stdin.readline().split("|")
            self.matrix.append([float(i) for i in line[0].split()])
            self.vect.append(float(line[1]))
            # add of the vector to the matrix
        for i in range(self.dim):
            self.matrix[i].append(self.vect[i])

    def solution(self):
        # upper triangular matrix from the gauss class
        try:
            self.getData(self.file)
            matrixT1 = Gauss(self.file).triangularize(self.dim, self.matrix)
            result = list()

            # modification of the matrix to the diagonal values to 1
            try:
                for i in range(self.dim):
                    coef = matrixT1[i][i]
                    matrixT1[i] = [(1 / coef) * i for i in matrixT1[i]]
            except ZeroDivisionError:
                return "Division par zéro"

            # last step output diagonal matrix of 1
            for i in range(self.dim - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    coef = matrixT1[j][i]
                    for k in range(self.dim + 1):
                        matrixT1[j][k] = (matrixT1[j][k] - coef * matrixT1[i][k])

            for i in range(self.dim):
                result.append(round(matrixT1[i][self.dim], 2))

            return result
        except ZeroDivisionError:
            return "division per zéro"
        except RuntimeError:
            return "Erreur lors de l'execution"
        except TypeError:
            return "Données non valables"
        except IndexError:
            return "Erreur lors de l'indexation"
        except EOFError:
            return "Eof error"
        except ValueError:
            return "Erreur lors de la saisie"
