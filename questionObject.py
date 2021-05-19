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
        # SECURE_PROGRAMMING_SOLUTION: checking that questionNumber is integer instance.
        if isinstance(questionNumber, int):
            self.__questionNumber = questionNumber
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: questionNumber is not an integer and cannot be inserted to the question object.")

    def getQuestionNumber(self):
        return self.__questionNumber

    def setQuestion(self, question):
        # SECURE_PROGRAMMING_SOLUTION: checking that question is string instance.
        if isinstance(question, str):
            self.__question = question
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: question is not a string and cannot be inserted to the question object.")

    def getQuestion(self):
        return self.__question

    def setAnswerOptions(self, answerOptions):
        # SECURE_PROGRAMMING_SOLUTION: checking that answerOptions is dictionary instance.
        if isinstance(answerOptions, dict):
            self.__answerOptions = answerOptions
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: answerOptions is not a dict and cannot be inserted to the question object.")

    def getAnswerOptions(self):
        return self.__answerOptions

    def setRightAnswer(self, rightAnswer):
        # SECURE_PROGRAMMING_SOLUTION: checking that rightAnswer is string instance.
        if isinstance(rightAnswer, str):
            self.__rightAnswer = rightAnswer
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: rightAnswer is not a string and cannot be inserted to the question object.")

    def getRightAnswer(self):
        return self.__rightAnswer

    def setPoints(self, points):
        # SECURE_PROGRAMMING_SOLUTION: checking that points is integer instance.
        if isinstance(points, int):
            self.__points = points
        else:
            # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
            print("Error: points is not an integer and cannot be inserted to the question object.")

    def getPoints(self):
        return self.__points

    def printQuestionWithNumber(self):
        print("{}. ".format(self.__questionNumber) + self.__question)

    def printObject(self):
        print("{}. ".format(self.__questionNumber) + str(self.__question) + " " + str(self.__answerOptions) + " " + str(self.__rightAnswer))
