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

        

class Algorithm():
    def __init__(self, matrix):
        self.matrix = matrix
        
        self.printMatrix(self.matrix)

    def printMatrix(self, matrix):
        print(matrix)
        for i in matrix:
            for j in matrix:
                print(matrix[i][j])

    def run(self, fromNode, toNode):
        print("da")