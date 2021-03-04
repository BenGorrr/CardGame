from player import Player
from card import Card
from config import *
import random
from operator import attrgetter

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
            p = Player(name, cards[:18])
            cards = cards[18:]
        else:
            p = Player(name, cards[:17])
            cards = cards[17:]
        players.append(p)

    printAvailableCards(players)
    input("Press ENTER to start.")

    #Phase-1 3-rounds
    startGame(players, 3)
    print(f"\n\n***** {players[0].name} and {players[1].name} proceed to 2-Player phase *****")

    input("Press ENTER to enter Phase-2.")
    print("******************")
    print("* 2-Player Phase *")
    print("******************")
    #Phase-2 4-rounds
    cards = create_deck() #create 52 cards
    random.shuffle(cards)
    for p in players:
        p.cards = cards[:26]
        cards = cards[26:]

    printAvailableCards(players)
    startGame(players, 4)
    print(f"***** {players[0].name} is the WINNER! *****")

def startGame(players, rounds):
    for round in range(1, rounds+1):
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

        #If current round is not the last round
        if round != rounds: input("\nPress ENTER to next round.")

        #before round end remove first 5 cards from all players
        for p in players:
            p.cards = p.cards[5:]
        printAvailableCards(players)

    players.remove(min(players, key=attrgetter('score')))

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
