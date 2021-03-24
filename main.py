from game import Game
from player import Player
from validator import *


def main():
    playersList = []

    try:
        amountOfPlayersString = str(input("Enter amount of wanted players (2-4): "))
    except ValueError:
        print("User input cannot be casted as a string, something is horrible wrong!")
        return
    # User input must be validate to be in accepted range of player amount
    if isValidPlayerAmount(amountOfPlayersString):
        amountOfPlayers = int(amountOfPlayersString)

        playerNumber = 1
        i = 0
        while i < amountOfPlayers:
            playername = input("Enter username of {}. player: ".format(playerNumber))
            if not isValidPlayerName(playername):
                return
            player = Player(playerNumber, playername)
            playersList.append(player)
            playerNumber = playerNumber + 1
            i = i + 1

        game = Game(amountOfPlayers, playersList)
        game.startGame()
main()