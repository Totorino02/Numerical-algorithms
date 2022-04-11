"""
    Name: LU.py
    Goal: Numerical resolution of linear equations with decomposition of Crout
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 02/02/2022
"""
import sys
from os.path import dirname, join


class Doolittle:

    def __init__(self, file):
        self.vect = None
        self.matrix = None
        self.file = join(dirname(__file__), file)
        self.dim = self.countLine()

    def countLine(self):
        """
            :return: nbOfLine
        """
        cpt = 0
        with open(self.file) as f:
            for line in f:
                if not line.isspace():
                    cpt += 1
        return cpt

    def getData(self, file):
        sys.stdin = open(file)
        self.matrix = list()
        self.vect = list()

        # Read data from the file
        for _ in range(self.dim):
            line = sys.stdin.readline().split("|")
            self.matrix.append([float(i) for i in line[0].split()])
            self.vect.append(float(line[1]))

    def inversion(self, i, mat, all=False):
        tempCtab = mat[i][i]
        maxValIndex = i
        for cpt in range(i, self.dim):
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
        dim = self.dim
        matrixL = list()
        matrixU = list()
        for i in range(dim):
            matrixL.append([0 for i in range(dim)])
            matrixU.append([0 for i in range(dim)])
        self.inversion(0, self.matrix)
        for i in range(self.dim):
            temp1 = round(self.matrix[i][0], 2)
            matrixL[i][0] = temp1
            temp2 = round((self.matrix[0][i]) / (matrixL[0][0]), 2)
            matrixU[0][i] = temp2
        for i in range(self.dim):
            matrixU[i][i] = 1

        # triangularize the matrix
        for i in range(1, self.dim):
            for q in range(i, self.dim):
                S1 = 0
                for k in range(i):
                    S1 += matrixL[q][k] * matrixU[k][i]
                matrixL[q][i] = self.matrix[q][i] - S1
            if matrixL[i][i] == 0:
                self.inversion(i, matrixL, True)
            for j in range(i + 1, self.dim):
                S2 = 0
                for k in range(i):
                    S2 += matrixL[i][k] * matrixU[k][j]
                    # print("Multi:  ", i, matrixL[i][k], " * ", matrixU[k][j])
                matrixU[i][j] = (self.matrix[i][j] - S2) / matrixL[i][i]
                # print("MatU val:", self.matrix[i][j], S2, matrixL[i][i], matrixU[i][j])

        return matrixL, matrixU

    def showMatrixL(self, matrixL):
        """
            :return:
        """
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(matrixL[_][i]), end="")  # the 7.2f is arbitrary
            print("\n")

    def showMatrixU(self, matrixU):
        """
            :return:
        """
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(matrixU[_][i]), end="")  # the 7.2f is arbitrary
            print("\n")

    def solution(self):
        """
            :return: solution
        """
        try:
            self.getData(self.file)
            matrixL, matrixU = self.triangularize()
            sY = list()
            sY.append(self.vect[0] / matrixL[0][0])
            try:
                for i in range(1, self.dim):
                    s1 = 0
                    for k in range(i):
                        temp = matrixL[i][k] * sY[k]
                        s1 += temp
                    val = (self.vect[i] - s1) / matrixL[i][i]
                    sY.append(val)
            except ZeroDivisionError:
                return "Division par zero"
            # lTM => s
            s = list()
            s.append(sY[self.dim - 1])
            for i in range(self.dim - 2, -1, -1):
                s1 = 0
                try:
                    for k in range(self.dim - 1, i, -1):
                        temp = matrixU[i][k] * s[self.dim - k - 1]
                        s1 += temp
                except:
                    return "erreur"
                try:
                    if matrixU[i][i] == 0:
                        return "Doulit division par zéro"
                    val = (sY[i] - s1) / matrixU[i][i]
                except ZeroDivisionError:
                    return "Veillez réessayer"
                s.append(val)
            s = [round(i, 2) for i in s]
            s.reverse()
            return s
        except ZeroDivisionError:
            return "division per zéro"
        except RuntimeError:
            return "Erreur lors de l'execution"
        except TypeError:
            return "Données non valables (infinie ou alphabétique)"
        except IndexError:
            return "Erreur lors de l'indexation"
        except EOFError:
            return "Eof error"
        except ValueError:
            return "Erreur lors de la saisie"
        except:
            print("Erreur lors de l'execution")
