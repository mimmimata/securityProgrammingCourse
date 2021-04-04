from validator import *
from fileReader import FileReader

class Game:

    def __init__(self, amountOfPlayers, players):
        self.__numberOfPlayers = amountOfPlayers
        self.__players = []
        self.setPlayers(players)
        self.__fileReader = FileReader()
        self.__questionsDict = {}
        self.__round = 1
        self.__playersNumberOnTurn = 0

    def setPlayers(self, players):
        if isinstance(players, list):
            if len(players) > self.__numberOfPlayers:
                print("Error: could not add more players that what is set to be amount of players. Game over")
            else:
                self.__players = players
        else:
            print("Error: players variable is not a list")

    def startGame(self):
        self.__playersNumberOnTurn = 0
        isThereAFile = input("Do you have your own question file? no/yes ")
        if isValidAswerForOwnQuestionFile(isThereAFile):
            if isThereAFile == "no":
                self.initializeQuestions("readyQuestions.txt")
            elif isThereAFile == "yes":
                fileUserWantsToUse = input("Enter question file: ")
                if isValidFileName(fileUserWantsToUse):
                    self.initializeQuestions(fileUserWantsToUse)
                else:
                    print("Invalid file name! Game is terminated!")
                    return
            self.runGame()
        else:
            print("Error: Incorrect input. Please enter 'no' or 'yes'")

    def initializeQuestions(self, fileName):
        self.__fileReader.addFileToRead(fileName)
        questions = self.__fileReader.readFile(fileName)
        if questions is not None:
            self.__questionsDict = questions

    def runGame(self):
        while self.__round <= len(self.__questionsDict):
            self.askQuestion()
            self.__round = self.__round + 1
            self.nextPlayer()

        self.endGame()


    def askQuestion(self):
        question = self.__questionsDict[str(self.__round)]
        question.printQuestionWithNumber()
        answerOptions = question.getAnswerOptions()
        for answerOption in answerOptions:
            print("{}. ".format(answerOption) + answerOptions[answerOption])
        answer = input("{} input the correct answer (to see players points, press 's'): ".format(self.__players[self.__playersNumberOnTurn].getName()))
        if isValidAnswer(answer):
            if answer == 's':
                self.printPlayersPoints()
                self.askQuestion()
            elif answer == question.getRightAnswer():
                self.__players[self.__playersNumberOnTurn].addPoints(question.getPoints())

        else:
            print("Invalid answer option! Use only a, b or c")
            self.askQuestion()

    def nextPlayer(self):
        nextPlayer = self.__playersNumberOnTurn + 1
        if nextPlayer >= self.__numberOfPlayers:
            self.__playersNumberOnTurn = 0
        else:
            self.__playersNumberOnTurn = nextPlayer

    def printPlayersPoints(self):
        # Using for .. in structure it makes sure that any buffer overflows or off by one
        # vulnerabilities not arise because list is looped element by element not with size and counter.
        for player in self.__players:
            print("Player {} has {} points.".format(player.getName(), str(player.getPoints())))

    def endGame(self):
        print("Game over!")
        self.printPlayersPoints()
        winnerPoints = 0
        winner = self.__players[0]
        for player in self.__players:
            if player.getPoints() > winnerPoints:
                winner = player
                winnerPoints = player.getPoints()

        print("The winner is: {}".format(winner.getName()))