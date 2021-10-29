from config import *

class Card():

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
        self.spoints = SUITES.index(self.suite)
        #self.fpoints = FACES.index(self.face) + 1
        self.fpoints = FACES.index(self.face) + 1 if FACES.index(self.face) < 9 else 10
        self.cardStr = self.suite + self.face
        #self.points = self.toPoints()

    def toPoints(self):
        return FACES.index(self.face) + 1

    def __str__(self):
        return f"Card: {self.suite + self.face}"

    def __repr__(self):
        return self.suite + self.face
