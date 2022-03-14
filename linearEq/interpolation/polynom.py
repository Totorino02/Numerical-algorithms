"""
    Name: polynom.py
    Goal: operations with of polynoms
    Author: HOUNSI madouvi antoine-sebastien
    Date: 8/03/2022
"""


class Polynom:

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


p1 = Polynom().mult([1], [0 / -2, 1 / -2])
p2 = Polynom().mult(p1, [-1 / -3, 1 / -3])
p3 = Polynom().mult(p2, [-2 / -4, 1 / -4])

"""print(p3)
print(Polynom().build(p3))
"""