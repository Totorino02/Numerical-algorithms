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
    def __init__(self, file):
        self.dim = self.countLine(file)
        self.matrixV(file)

    def matrixV(self,file):
        try:
            self.vect= list()
            self.matrix = list()
            sys.stdin = open(file)
            for _ in range(self.dim):
                line = sys.stdin.readline().split("|")
                self.matrix.append([(float)(i) for i in line[0].split()])
                self.vect.append(float(line[1]))
            #add of the vector
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
        dim = self.dim; vect = self.vect; matrix = self.matrix
        try:
            for i in range(dim):
                for j in range(i+1, dim):
                    cpt = i
                    while matrix[i][i] == 0 :
                        # inversion if the begin of the pivot is null: L_i <-> L_cpt
                        temporalTab = [x for x in matrix[i]]
                        matrix[i] = [x for x in matrix[cpt+1]]
                        matrix[cpt + 1] = [x for x in temporalTab]
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
                print("Il existe une infinité de solution")
                return
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
            print(self.results)
        except ZeroDivisionError:
            print("division per zéro")

    def showTM(self):
        for _ in range(self.dim):
            for i in range(self.dim):
                print('{:7.2f}'.format(self.matrix[_][i]), end="") # the 7.2f is arbitrary
            print("\n")

