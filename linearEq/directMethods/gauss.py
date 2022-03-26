"""
    Name: gauss.py
    Goal: Numerical resolution of linear equations with the method of Gauss
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 29/01/2022
"""

import sys
from os.path import dirname, join
import numpy as np


class Gauss:
    """
        Numerical resolution of linear equations with the method of Gauss
    """

    def __init__(self, file):
        self.matrix = None
        self.vect = None
        self.file = join(dirname(__file__), file)
        self.dim = self.countLine(self.file)

    def getData(self, file):
        try:
            self.vect = list()
            self.matrix = list()
            sys.stdin = open(file)
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([float(i) for i in line[0].split()])
                self.vect.append(float(line[1]))
            # add of the vector
            for i in range(self.dim):
                self.matrix[i].append(self.vect[i])
        except TypeError:
            print("Type Error :=> incorrect input")
        except RuntimeError:
            print("Runtime Error :=> Run time error please try aigain")
        except ValueError:
            print("Value Error :=> you enter innapropriate value")
        except IndexError:
            print("Index Error :=> not square matrix !")

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

    def triangularize(self, dim, matrix):
        matrixT = list()
        for i in range(dim):
            matrixT.append(matrix[i])
        for i in range(dim):
            for j in range(i + 1, dim):

                # inversion if the begin of the pivot is null: L_i <-> L_cpt
                while matrixT[i][i] == 0:
                    tempCtab = matrixT[i][i]
                    maxValIndex = i
                    for cpt in range(i, dim):
                        if abs(matrixT[cpt][i]) > tempCtab:
                            maxValIndex = cpt
                    temporalTab = [x for x in matrixT[i]]
                    matrixT[i] = [x for x in matrixT[maxValIndex]]
                    matrixT[maxValIndex] = [x for x in temporalTab]
                #
                if matrixT[j][i] != 0:
                    fMultiplicatif = -(matrixT[i][i] / matrixT[j][i])
                    matrixT[j] = [(fMultiplicatif * x) for x in matrixT[j]]

                    # last step of the modification the value
                    for k in range(i, dim + 1):
                        matrixT[j][k] = (matrixT[i][k] + matrixT[j][k])
        return matrixT

    def solution(self):
        try:
            self.getData(self.file)
            matrix = self.triangularize(self.dim, self.matrix)
            dim = self.dim
            vect = np.zeros(dim)
            for i in range(dim):
                vect[i] = matrix[i][dim]
                matrix[i].pop(dim)
            results = list()

            # impossibility of the solution
            for i in range(dim - 1, -1, -1):
                if matrix[i][i] == 0:
                    if i == dim - 1:
                        if vect[i] != 0:
                            return "Solution impossible"
                        elif vect[i] == 0:
                            return "Il existe une infinité de solution"
                    return "Il existe une infinité de solution"

            # unique solution
            results.append(round(vect[dim - 1] / matrix[dim - 1][dim - 1], 2))
            for i in range(dim - 2, -1, -1):
                n = len(results)
                x = 0
                for k in range(dim - 1, dim - n - 1, -1):
                    x += matrix[i][k] * results[dim - 1 - k]
                res = (vect[i] - x) / (matrix[i][i])
                results.append(round(res, 2))
            results.reverse()
            return results
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

    def showTM(self):
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(self.matrix[_][i]), end="")  # the 7.2f is arbitrary
            print("\n")
