from validator import *
from fileReader import FileReader

"""
This class contains actual game logic.
"""
class Game:

    def __init__(self, amountOfPlayers, players):
        self.__numberOfPlayers = amountOfPlayers
        self.__players = []
        self.setPlayers(players)
        self.__fileReader = FileReader()
        self.__questionsDict = {}
        self.__round = 1
        self.__playersNumberOnTurn = 0
        self.__originalQuestionFileName = "myQuestions.txt"

    """
    Sets players.
    @:parameter players list of players
    """
    def setPlayers(self, players):
        # SECURE_PROGRAMMING_SOLUTION: checking that players is list instance.
        if isinstance(players, list):
            # SECURE_PROGRAMMING_SOLUTION: checking that no more than amount of players are added.
            if len(players) > self.__numberOfPlayers:
                # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
                print("Error: could not add more players that what is set to be amount of players.")
            else:
                self.__players = players
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: players variable is not a list")

    """
    Starts the game asking the question file and initializing questions.
    """
    def startGame(self):
        isThereAFile = input("Do you have your own question file? no/yes ")
        # SECURE_PROGRAMMING_SOLUTION: validating user input.
        if isValidAswerForOwnQuestionFile(isThereAFile):
            if isThereAFile == "no":
                self.initializeQuestions(self.__originalQuestionFileName)
            elif isThereAFile == "yes":
                while True:
                    fileUserWantsToUse = input("Enter question file: ")
                    # SECURE_PROGRAMMING_SOLUTION: validating user input.
                    if isValidFileName(fileUserWantsToUse):
                        self.initializeQuestions(fileUserWantsToUse)
                        break
                    elif fileUserWantsToUse == "no":
                        self.initializeQuestions(self.__originalQuestionFileName)
                        break
                    else:
                        # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
                        print("Error: Invalid file! Please enter correct file name or enter 'no' if you want to continue with file in game!")

            if len(self.__questionsDict) == 0:
                # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
                print("Error: No questions on game because there occured a problem during reading the question file!")
                self.startGame()
            else:
                self.runGame()
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: Incorrect input. Please enter 'no' or 'yes'")
            self.startGame()

    """
    Initialize questions.
    @:parameter fileName name of the question file.
    """
    def initializeQuestions(self, fileName):
        questions = self.__fileReader.readFile(fileName)
        # SECURE_PROGRAMMING_SOLUTION: None is not initialized for questions.
        if questions is not None:
            self.__questionsDict = questions

    """
    Runs the game by asking question and changing the player and finally when questions end, ends the game.
    """
    def runGame(self):
        while self.__round <= len(self.__questionsDict):
            self.askQuestion()
            self.__round = self.__round + 1
            self.nextPlayer()

        self.endGame()

    """
    Printing question, its' answer options and adding points to player if answer was right.  
    """
    def askQuestion(self):
        question = self.__questionsDict[str(self.__round)]
        question.printQuestionWithNumber()
        answerOptions = question.getAnswerOptions()

        # SECURE_PROGRAMMING_SOLUTION: No off by one vulnerability can arise when looping is done this way.
        for answerOption in answerOptions:
            print("{}. ".format(answerOption) + answerOptions[answerOption])

        answer = input("{} input the correct answer (to see players points, press 's'): ".format(self.__players[self.__playersNumberOnTurn].getName()))
        # SECURE_PROGRAMMING_SOLUTION: validating user input.
        if isValidAnswer(answer):
            if answer == 's':
                self.printPlayersPoints()
                self.askQuestion()
            elif answer == question.getRightAnswer():
                self.__players[self.__playersNumberOnTurn].addPoints(question.getPoints())

        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: Invalid answer option! Use only a, b or c")
            self.askQuestion()

    """
    Changing to the next player.
    """
    def nextPlayer(self):
        nextPlayer = self.__playersNumberOnTurn + 1
        if nextPlayer >= self.__numberOfPlayers:
            self.__playersNumberOnTurn = 0
        else:
            self.__playersNumberOnTurn = nextPlayer

    """
    Prints player name and point amount.
    """
    def printPlayersPoints(self):
        # SECURE_PROGRAMMING_SOLUTION: Using for .. in structure it makes sure that any buffer overflows or off by one
        # vulnerabilities not arise because list is looped element by element not with size and counter.
        for player in self.__players:
            print("Player {} has {} points.".format(player.getName(), str(player.getPoints())))

    """
    Everything that it is need to be done when game ends.
    """
    def endGame(self):
        print("Game over!")
        self.printPlayersPoints()
        winnerPoints = 0

        # SECURE_PROGRAMMING_SOLUTION: No off by one vulnerability can arise when checking that self.__players lenght
        # is not zero before getting first item out of it.
        if len(self.__players) != 0:
            winner = self.__players[0]

        # SECURE_PROGRAMMING_SOLUTION: No off by one vulnerability can arise when looping is done this way.
        for player in self.__players:
            if player.getPoints() > winnerPoints:
                winner = player
                winnerPoints = player.getPoints()

        playersWithSamePointAmount = []
        # SECURE_PROGRAMMING_SOLUTION: No off by one vulnerability can arise when looping is done this way.
        for player in self.__players:
            if player.getPoints() == winner.getPoints():
                playersWithSamePointAmount.append(player)

        if len(playersWithSamePointAmount) > 1:
            print("Game is tie with players: ")
            # SECURE_PROGRAMMING_SOLUTION: No off by one vulnerability can arise when looping is done this way.
            for player in playersWithSamePointAmount:
                print("- {}".format(player.getName()))
        else:
            print("The winner is: {}".format(winner.getName()))
