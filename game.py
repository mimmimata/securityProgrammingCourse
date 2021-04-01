from gameStatus import *
from validator import *
from fileReader import FileReader

class Game:

    def __init__(self, amountOfPlayers, players):
        self.__numberOfPlayers = amountOfPlayers
        self.__players = []
        self.setPlayers(players)
        self.__gameStateObject = GameState()
        self.__fileReader = FileReader()

    def setPlayers(self, players):
        if isinstance(players, list):
            if len(players) > self.__numberOfPlayers:
                print("Error: could not add more players that what is set to be amount of players. Game over")
            else:
                self.__players = players
        else:
            print("Error: players variable is not a list")

    def startGame(self):
        print("game started")
        self.printPlayers()
        isThereAFile = input("Do you have your own question file? no/yes ")
        if isValidAswerForOwnQuestionFile(isThereAFile):
            if isThereAFile == "no":
                self.__fileReader.addFileToRead("readyQuestions.txt")
                self.__fileReader.readFile("readyQuestions.txt")
            # DO something real



            pass
        else:
            print("Error: Incorrect input. Please enter 'no' or 'yes'")




    def printPlayers(self):
        # Using for .. in structure it makes sure that any buffer overflows or off by one
        # vulnerabilities not arise because list is looped element by element not with size and counter.
        for player in self.__players:
            player.printPlayer()

    def endGame(self):
        # If some one has for example ten points, then game is over
        print("game over")