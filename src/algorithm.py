import math

class Coordinate():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def isEqual(self, that):
        return self.i == that.i and self.j == that.j

    def distanceTo(self, that):
        return math.sqrt(((self.i - that.i) ** 2) + ((self.j - that.j) ** 2))

    def toString(self):
        return str("[" + self.i + ", " + self.j + "]")

    def range(self, fromNode, toNode):
        return (fromNode.i <= self.i and self.i <= toNode.i and fromNode.j <= self.j and self.j <= toNode.j)

    def surrounding(self):
        return [
            Coordinate(self.i - 1, self.j + 1),
            Coordinate(self.i, self.j + 1),
            Coordinate(self.i + 1, self.j + 1),
            Coordinate(self.i + 1, self.j),
            Coordinate(self.i + 1, self.j - 1),
            Coordinate(self.i, self.j - 1),
            Coordinate(self.i - 1, self.j - 1),
            Coordinate(self.i - 1, self.j)
        ]

class Node():
    def __init__(self, coord):
        self.coord = coord

        self.parentNode = None
        self.childrenNodes = []
        self.goalNode = None

        self.g = 0
        self.h = None
        self.f = None

        self.index = 0

    def addParent(self, parent):
        if parent is not None:
            self.index = parent.index + 1
            self.parentNode = parent
            self.parentNode.addChild(self)
            self.g = self.coord.distanceTo(self.parentNode.coord) + self.parentNode.g
        else:
            self.index = 0
            self.g = 0
        return self

    def removeParent(self):
        if self.parentNode is not None:
            self.parentNode.removeChild(self)
            self.parentNode = None
            self.g = 0
        return self

    def addChild(self, child):
        self.childrenNodes.append(child)

    def removeChild(self, child):
        

class AStar():
    def __init__(self, matrix):
        self.matrix = matrix
        print("hello")
        coord = Coordinate(1, 2)
        print(coord.i)

    def run(self, fromNode, toNode):
        print("da")