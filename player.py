from config import *

class Player():

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.score = 0

    def cardsOnHand(self, n=None, sort=False):
        if not n:
            n = len(self.cards)
        cards = self.cards.copy()[:n]
        if sort:
            cards = self.sortCards(cards)
        cards_str = ""
        for c in cards:
            cards_str += repr(c)
            if (cards.index(c) + 1) % 5 == 0 and cards.index(c) + 1 != n:
                cards_str += ", "
            else:
                 cards_str += " "
        return cards_str

    #Sort with suite then face
    def sortCards(self, cards):
        cards.sort(key=lambda x: (x.spoints, x.fpoints))
        #print("Sorted: ", cards, self.cards)
        return cards

    def shuffleCards(self):
        random.shuffle(self.cards)

    def toPoints(self, cards):
        cards = self.sortCards(cards)
        suiteOccurrance = [("d", sum('d' in card.cardStr for card in cards)), ("c", sum('c' in card.cardStr for card in cards)), ("h", sum('h' in card.cardStr for card in cards)), ("s", sum('s' in card.cardStr for card in cards))]
        suiteOccurrance.sort(key=lambda x: x[1],reverse=True)
        #two same occurance
        if suiteOccurrance[0][1] == 2 and suiteOccurrance[1][1] == 2:
            if SUITES.index(suiteOccurrance[0][0]) > SUITES.index(suiteOccurrance[1][0]): suite = suiteOccurrance[0][0]
            else: suite = suiteOccurrance[1][0]
        else:
            suite = suiteOccurrance[0][0]
        return sum(card.fpoints for card in cards if suite in card.cardStr)

    #toString() equivalent
    def __str__(self):
        return f"Name: {self.name} Cards On Hand: {self.cards}"
