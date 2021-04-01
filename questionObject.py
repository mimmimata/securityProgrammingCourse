# Class to hold information for one question
class questionObject:

    def __init__(self, questionNumber, question, answerOptions, rightAnswer):
        self.__questionNumber = questionNumber
        self.__question = question
        self.__answerOptions = answerOptions
        self.__rightAnswer = rightAnswer

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
        return self.__AnswerOptions

    def setRightAnswer(self, rightAnswer):
        if isinstance(rightAnswer, str):
            self.__rightAnswer = rightAnswer

    def getRightAnswer(self):
        return self.__rightAnswer

    def printQuestionWithNumber(self):
        print(self.__questionNumber + " " + self.__question)

    def printObject(self):
        return str(self.__questionNumber) + " " + str(self.__question) + " " + str(self.__answerOptions) + " " + str(self.__rightAnswer)
