"""
    Name: polynom.py
    Goal: operations with of polynoms
    Author: HOUNSI madouvi antoine-sebastien
    Date: 8/03/2022
"""


class Polynom:

    # def __init__(self):

    def mult(self, P1, P2):
        """ Multiplication between P1 and P2 """
        maxArray = [x for x in P1]
        minArray = [x for x in P2]
        if len(P1) == 1 or len(P2) == 1:
            if len(P1) == 1:
                return [P1[0] * x for x in P2]
            else:
                return [P2[0] * x for x in P1]
        diffLength = len(P1) - len(P2)
        if diffLength > 0:
            maxArray = [x for x in P1]
            minArray = [x for x in P2]
            for i in range(abs(diffLength)):
                minArray.append(0)
        elif diffLength < 0:
            minArray = [x for x in P1]
            maxArray = [x for x in P2]
            maxArray.index(2)
            for i in range(abs(diffLength)):
                minArray.append(0)
        minArray.append(0)
        maxArray.append(0)
        result = list()
        length = len(maxArray)
        for i in range(length):
            cpt = 0
            for j in range(i + 1):
                val = maxArray[j] * minArray[i - j]
                cpt += val
            result.append(cpt)
        result.reverse()
        return result

    def add(self, P1, P2, neg=False):
        """Addition between P1 and P2"""
        maxArray = [x for x in P1]
        minArray = [x for x in P2]
        diffLength = len(P1) - len(P2)
        if diffLength > 0:
            maxArray = [x for x in P1]
            minArray = [x for x in P2]
            for i in range(abs(diffLength)):
                minArray.append(0)
        elif diffLength < 0:
            minArray = [x for x in P1]
            maxArray = [x for x in P2]
            for i in range(abs(diffLength)):
                minArray.append(0)
        result = list()
        length = len(maxArray)
        for i in range(length):
            result.append(maxArray[i] + minArray[i])
        return result

    def build(self, tab):
        str = ""
        length = len(tab)
        for i in range(length):
            if i == 0:
                if tab[i] > 0:
                    str += "({0})".format(tab[i])
                elif tab[i] < 0:
                    str += "-({0})".format(-tab[i])
            elif i == 1:
                if tab[i] > 0:
                    str += "+({0}*X)".format(tab[i])
                elif tab[i] < 0:
                    str += "-({0}*X)".format(-tab[i])
            else:
                if tab[i] > 0:
                    str += "+({0}*X**{1})".format(tab[i], i)
                elif tab[i] < 0:
                    str += "-({0}*X**{1})".format(-tab[i], i)
        return str

    def div(self, P1, P2):
        """Euclidian division between P1 and P2"""



p0 = Polynom().mult([-1, 1], [1])
p1 = Polynom().mult([-1, 1], [-1, 1])
p2 = Polynom().mult(p1, [-1, 1])
p3 = Polynom().mult(p2, [-1, 1])
p4 = Polynom().mult(p3, [-1, 1])
p5 = Polynom().mult(p4, [-1, 1])
p6 = Polynom().mult(p5, [-1, 1])
p7 = Polynom().mult(p6, [-1, 1])
p8 = Polynom().mult(p7, [-1, 1])
p9 = Polynom().mult(p8, [-1, 1])
p10 = Polynom().mult(p9, [-1, 1])
p11 = Polynom().mult(p10, [-1, 1])
print(p0)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)
print(Polynom().build(p11))


# print(p1)
# print(p2)
