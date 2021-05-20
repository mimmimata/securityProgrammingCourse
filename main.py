from game import Game
from player import Player
from validator import *

"""
main function that starst the program.
"""
def main():
    playersList = []

    while True:
        try:
            amountOfPlayersString = str(input("Enter amount of wanted players (2-4): "))
        # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
        except ValueError:
            print("Error: User input cannot be casted as a string, something is horrible wrong!")
            return

        # SECURE_PROGRAMMING_SOLUTION: validating user input.
        if isValidPlayerAmount(amountOfPlayersString):
            amountOfPlayers = int(amountOfPlayersString)
            break
        else:
            print("Error: Invalid number of players, player amount needs to be between 2 and 4.")

    playerNumber = 1
    while playerNumber <= amountOfPlayers:
        playername = input("Enter username of {}. player: ".format(playerNumber))
        # SECURE_PROGRAMMING_SOLUTION: validating user input and while not valid asking playername again.
        while not isValidPlayerName(playername):
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: Invalid player name, allowed characters A-Z and a-z and allowed name length is 20 characters.")
            playername = input("Enter username of {}. player: ".format(playerNumber))
        player = Player(playerNumber, playername)
        playersList.append(player)
        playerNumber = playerNumber + 1
    game = Game(amountOfPlayers, playersList)
    game.startGame()

main()