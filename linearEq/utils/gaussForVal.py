"""
    Name: gauss.py
    Goal: Numerical resolution of linear equations with the method of Gauss
    Author: HOUNSI Madouvi antoine-sebastien
    Date: 29/01/2022
"""

import sys
class gauss:
    """
        Numerical resolution of linear equations with the method of Gauss
    """
    def __init__(self, matrix, vect):
        self.dim = len(vect)
        self.vect = list()
        self.matrix = list()
        for i in range(self.dim):
            self.matrix.append([])
            for j in range(self.dim):
                self.matrix[i].append(matrix[i][j])
            self.vect.append(vect[i])
        for i in range(self.dim):
            self.matrix[i].append(self.vect[i])
        #self.showResult()

    def triangularize(self):
        dim = self.dim; vect = self.vect; matrix = self.matrix
        try:
            for i in range(dim):
                for j in range(i+1, dim):
                    cpt = i
                    while matrix[i][i] == 0 and cpt < dim :
                        # inversion if the begin of the pivot is null: L_i <-> L_cpt
                        tempCtab = matrix[i][i]
                        maxValIndex = i
                        for cpt in range(i, dim):
                            if abs(matrix[cpt][i]) > tempCtab:
                                maxValIndex = cpt
                        temporalTab = [x for x in self.matrix[i]]
                        self.matrix[i] = [x for x in self.matrix[maxValIndex]]
                        self.matrix[maxValIndex] = [x for x in temporalTab]
                    if matrix[j][i] != 0:
                        fMultiplicatif = -(matrix[i][i]/matrix[j][i])
                        matrix[j] = [(fMultiplicatif * x) for x in matrix[j]]
                        #last step of the modification the value
                        for k in range(i, dim+1):
                            matrix[j][k] = (matrix[i][k] + matrix[j][k])
        except RuntimeError:
            return "Runtime Error"
        except TypeError:
            return "Type error"
        except IndexError:
            return "Index error"
        except EOFError:
            return "Eof error"
        return matrix

    def showResult(self):
        self.triangularize()
        matrix = self.matrix; vect = self.vect
        dim = self.dim
        for i in range(dim):
            vect[i] = matrix[i][dim]
            matrix[i].pop(dim)
        self.results = list()
        # impossibility of the solution
        noSolvable = 0
        for i in range(dim-1, -1, -1):
            if matrix[i][i] == 0:
                if i == dim-1:
                    if vect[i] != 0:
                        print("Solution impossible")
                        return
                    elif vect[i] == 0:
                        print("Il existe une infinité de solution")
                        return
                raise ValueError("Il existe une infinité de solution")
        #unique solution
        try:
            self.results.append(round(vect[dim-1]/matrix[dim-1][dim-1],2))
            for i in range(dim-2, -1, -1):
                n = len(self.results)
                x = 0
                for k in range(dim-1, dim-n-1, -1):
                    x += matrix[i][k]*self.results[dim-1-k]
                res = (vect[i] -x)/(matrix[i][i])
                self.results.append(round(res,2))
            self.results.reverse()
            return self.results
        except ZeroDivisionError:
            print("division per zéro")

