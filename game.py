from player import Player
from card import Card
from config import *
import random

def main():
    #Init var
    players = [] #players list
    cards = create_deck() #create 52 cards
    #game start with Phase 1 (3 player game)
    print("******************")
    print("* 3-Player Phase *")
    print("******************")

    #Get players name
    random.shuffle(cards)
    for i in range(3):
        name = input(f"Enter player {i+1} name: ")
        if i == 0:
            p = Player(name, cards[0:18])
            cards = cards[18:]
        else:
            p = Player(name, cards[0:17])
            cards = cards[17:]
        players.append(p)

    printAvailableCards(players)

    input("Press ENTER to start.")

    #3 rounds
    for round in range(1, 4):
        print(f'\n\n*** ROUND {round} ***')
        print("Cards at Hand:")
        #print(max([player.toPoints(player.cards[:5]) for player in players]))
        round_players = [(player, player.toPoints(player.cards[:5].copy())) for player in players]
        for p in round_players:
            print(f"\n{p[0].name}\t: {p[0].cardsOnHand(5, True)} | Point = {p[1]}", end='')
            if p[1] == max([player[1] for player in round_players]):
                print(" | Win", end='')
                p[0].score += p[1]

        print("\n\nScore:")
        for p in round_players:
            print(f"{p[0].name}\t= {p[0].score}")

        input("\nPress ENTER to next round.")
        #before round end remove first 5 cards from all players
        for p in players:
            p.cards = p.cards[5:]
        printAvailableCards(players)

def startGame(players, round):
    pass

def printAvailableCards(players):
    print("\nAvailable Cards:")
    for p in players:
        print(f"{p.name}\t: {p.cardsOnHand()}")

def create_deck():
    all_cards = []
    for s in SUITES:
        for f in FACES:
            all_cards.append(Card(s, f))
    return all_cards

if __name__ == '__main__':
    main()
