from config import *

class Card():

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
        self.points = self.toPoints()

    def toPoints(self):
        return SUITES.index(self.suite) + FACES.index(self.face) + 2

    def __str__(self):
        return f"Card: {self.suite + self.face} Points: {self.points}"
