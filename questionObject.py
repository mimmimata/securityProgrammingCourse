"""
Class to hold information for one question.
"""
class questionObject:

    def __init__(self, questionNumber, question, answerOptions, rightAnswer):
        self.__questionNumber = questionNumber
        self.__question = question
        # AnswerOptions is dict which key: answerOptionCharacter as a string and value: string
        self.__answerOptions = answerOptions
        self.__rightAnswer = rightAnswer
        self.__points = 1

    def setQuestionNumber(self, questionNumber):
        if isinstance(questionNumber, int):
            self.__questionNumber = questionNumber
        else:
            print("Error: questionNumber is not an integer and cannot be inserted to the question object.")

    def getQuestionNumber(self):
        return self.__questionNumber

    def setQuestion(self, question):
        if isinstance(question, str):
            self.__question = question
        else:
            print("Error: question is not a string and cannot be inserted to the question object.")

    def getQuestion(self):
        return self.__question

    def setAnswerOptions(self, answerOptions):
        if isinstance(answerOptions, dict):
            self.__answerOptions = answerOptions
        else:
            print("Error: answerOptions is not a dict and cannot be inserted to the question object.")

    def getAnswerOptions(self):
        return self.__answerOptions

    def setRightAnswer(self, rightAnswer):
        if isinstance(rightAnswer, str):
            self.__rightAnswer = rightAnswer
        else:
            print("Error: rightAnswer is not a string and cannot be inserted to the question object.")

    def getRightAnswer(self):
        return self.__rightAnswer

    def setPoints(self, points):
        if isinstance(points, int):
            self.__points = points
        else:
            print("Error: points is not an integer and cannot be inserted to the question object.")

    def getPoints(self):
        return self.__points

    def printQuestionWithNumber(self):
        print("{}. ".format(self.__questionNumber) + self.__question)

    def printObject(self):
        print("{}. ".format(self.__questionNumber) + str(self.__question) + " " + str(self.__answerOptions) + " " + str(self.__rightAnswer))
