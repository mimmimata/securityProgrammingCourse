from game import Game
from player import Player
from validator import *


def main():
    playersList = []

    while True:
        try:
            amountOfPlayersString = str(input("Enter amount of wanted players (2-4): "))
        except ValueError:
            print("User input cannot be casted as a string, something is horrible wrong!")
            return

        # User input must be validate to be in accepted range of player amount
        if isValidPlayerAmount(amountOfPlayersString):
            amountOfPlayers = int(amountOfPlayersString)
            break
        else:
            print("Invalid number of players, player amount needs to be between 2 and 4.")
    playerNumber = 1
    i = 0
    while i < amountOfPlayers:
        playername = input("Enter username of {}. player: ".format(playerNumber))
        while not isValidPlayerName(playername):
            print("Error: Invalid player name, allowed characters A-Z and a-z and allowed name length is 20 characters.")
            playername = input("Enter username of {}. player: ".format(playerNumber))
        player = Player(playerNumber, playername)
        playersList.append(player)
        playerNumber = playerNumber + 1
        i = i + 1
    game = Game(amountOfPlayers, playersList)
    game.startGame()

main()