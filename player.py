
class Player():

    def __init__(self, name):
        self.name = name

    #toString() equivalent
    def __str__(self):
        return f"Name: {self.name}"
