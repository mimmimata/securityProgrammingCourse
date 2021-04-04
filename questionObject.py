# Class to hold information for one question
class questionObject:

    def __init__(self, questionNumber, question, answerOptions, rightAnswer):
        self.__questionNumber = questionNumber
        self.__question = question
        self.__answerOptions = answerOptions
        self.__rightAnswer = rightAnswer
        self.__points = 1

    def setQuestionNumber(self, questionNumber):
        if isinstance(questionNumber, int):
            self.__questionNumber = questionNumber

    def getQuestionNumber(self):
        return self.__questionNumber

    def setQuestion(self, question):
        if isinstance(question, str):
            self.__question = question

    def getQuestion(self):
        return self.__question

    def setAnswerOptions(self, answerOptions):
        if isinstance(answerOptions, dict):
            self.__answerOptions = answerOptions

    def getAnswerOptions(self):
        return self.__answerOptions

    def setRightAnswer(self, rightAnswer):
        if isinstance(rightAnswer, str):
            self.__rightAnswer = rightAnswer

    def getRightAnswer(self):
        return self.__rightAnswer

    def setPoints(self, points):
        if isinstance(points, int):
            self.__points = points

    def getPoints(self):
        return self.__points

    def printQuestionWithNumber(self):
        print("{}. ".format(self.__questionNumber) + self.__question)

    def printObject(self):
        print("{}. ".format(self.__questionNumber) + str(self.__question) + " " + str(self.__answerOptions) + " " + str(self.__rightAnswer))
