from player import Player
from config import *

def main():
    #Init var
    players = [] #players list
    cards = ["dA", "d2"]
    #game start with Phase 1 (3 player game)
    print("******************")
    print("* 3-Player Phase *")
    print("******************")

    #Get players name
    for i in range(3):
        name = input(f"Enter player {i+1} name: ")
        p = Player(name)
        players.append(p)

    for p in players:
        print(p)


if __name__ == '__main__':
    main()
