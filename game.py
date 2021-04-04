from gameStatus import *
from validator import *
from fileReader import FileReader
from questionObject import questionObject

class Game:

    def __init__(self, amountOfPlayers, players):
        self.__numberOfPlayers = amountOfPlayers
        self.__players = []
        self.setPlayers(players)
        self.__gameStateObject = GameState()
        self.__fileReader = FileReader()
        self.__questionsDict = {}
        self.__round = 1
        self.__playerOnTurn = None

    def setPlayers(self, players):
        if isinstance(players, list):
            if len(players) > self.__numberOfPlayers:
                print("Error: could not add more players that what is set to be amount of players. Game over")
            else:
                self.__players = players
        else:
            print("Error: players variable is not a list")

    def startGame(self):
        self.printPlayers()
        self.__playerOnTurn = self.__players[0]
        isThereAFile = input("Do you have your own question file? no/yes ")
        if isValidAswerForOwnQuestionFile(isThereAFile):
            if isThereAFile == "no":
                self.__fileReader.addFileToRead("readyQuestions.txt")
                questions = self.__fileReader.readFile("readyQuestions.txt")
                if questions is not None:
                    self.__questionsDict = questions
            self.runGame()
        else:
            print("Error: Incorrect input. Please enter 'no' or 'yes'")

    def runGame(self):
        while self.__round <= len(self.__questionsDict):
            question = self.__questionsDict[str(self.__round)]
            question.printQuestionWithNumber()
            answerOptions = question.getAnswerOptions()
            for answerOption in answerOptions:
                print("{}. ".format(answerOption) + answerOptions[answerOption])
            # TODO: validate user input!!!
            answer = input("{} input the correct answer: ".format(self.__playerOnTurn.getName()))


            self.__round = self.__round + 1
            pass

        self.endGame()


    def printPlayers(self):
        # Using for .. in structure it makes sure that any buffer overflows or off by one
        # vulnerabilities not arise because list is looped element by element not with size and counter.
        for player in self.__players:
            player.printPlayer()

    def endGame(self):
        # If some one has for example ten points, then game is over
        print("game over")