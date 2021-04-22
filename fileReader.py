from validator import *
from questionObject import questionObject

questionTextPart = "question: "
answerOptionsTextPart = "answer_options: "
rightAnswerTextPart = "correct_answer: "
leftBracketPart = "["
rightBracketPart = "]"

"""
Class for containing all functionality what is needed to read and parse question file.
"""
class FileReader:

    def __init__(self):
        self.__fileToRead = None
        # key: question number, value: questionObject
        self.__questionStructure = {}
        self.__maxFileLineAmount = 300

    def addFileToRead(self, fileName):
        if isValidFileName(fileName):
            self.__fileToRead = fileName

    def readFile(self, fileName):
        if isValidFileName(fileName):
            try:
                fileToRead = open(fileName, "r",  encoding="utf8")
                amountOfReadLines = 0
                if amountOfReadLines <= self.__maxFileLineAmount:
                    for line in fileToRead:
                        amountOfReadLines = amountOfReadLines + 1
                        if isValidFileLine(line):
                            parsedQuestionObject = self.parseLine(line, amountOfReadLines)
                            if parsedQuestionObject is not None:
                                self.__questionStructure[parsedQuestionObject.getQuestionNumber()] = parsedQuestionObject
                            else:
                                return None
                        else:
                            # parseLine is called even for not valid file line so user gets an accurate error message
                            # which tells where the problem is.
                            self.parseLine(line, amountOfReadLines)
                            return None
                fileToRead.close()

                return self.__questionStructure
            except FileNotFoundError:
                print("Cannot find file!")
                return None

    def parseLine(self, lineToParse, lineNumber):

        # answerOptionsDict: key: a,b or c and value: answer
        answerOptions = {}

        questionNumber = self.parseQuestionNumber(lineToParse, lineNumber)
        if questionNumber is not None:
            question = self.parseQuestion(lineToParse, lineNumber)
            if question is not None:
                #
                answerOptions = self.parseAswerOptions(lineToParse, answerOptions, lineNumber)
                if answerOptions is not None and len(answerOptions) > 0:
                    rightAnswer = self.parseCorrectAnswer(lineToParse, lineNumber)
                    if rightAnswer is not None:
                        readyQuestion = questionObject(questionNumber, question, answerOptions, rightAnswer)
                        return readyQuestion
        return None

    def parseQuestionNumber(self, lineToParse, lineNumber):
        questionNumberResultObject = re.search(questionNumberRegex, lineToParse)
        if questionNumberResultObject is not None:
            questionNumberAndDot = questionNumberResultObject.group()
            return questionNumberAndDot.replace(".", '')
        print("Error parsing line. Invalid or missing question number on line {} ".format(lineNumber))
        return None

    def parseQuestion(self, lineToParse, lineNumber):
        questionResultObject = re.search(questionPartRegex, lineToParse)
        if questionResultObject is not None:
            notParsedQuestion = questionResultObject.group()
            return notParsedQuestion.replace(questionTextPart, '')
        print("Error parsing line. Invalid or missing question on line {} ".format(lineNumber))
        return None

    def parseAswerOptions(self, lineToParse, answerOptions, lineNumber):
        answerOptionsResultObject = re.search(answerOptionsPartRegex, lineToParse)
        if answerOptionsResultObject is not None:
            notParsedAnswerOptions = answerOptionsResultObject.group()
            answerOptionsTextPartRemoved = notParsedAnswerOptions.replace(answerOptionsTextPart, '')
            splittedAnswerOptions = answerOptionsTextPartRemoved.split(rightBracketPart)
            for answerOptionPart in splittedAnswerOptions:
                answerOption = answerOptionPart.replace(leftBracketPart, '')
                if len(answerOption) > 3:
                    answerOptions[answerOption[0]] = answerOption[3:]
                elif len(answerOption) > 1:
                    answerOptions[answerOption[0]] = ''
            print(answerOptions)
            return answerOptions
        print("Error parsing line. Invalid or missing answer options on line {} ".format(lineNumber))
        return None

    def parseCorrectAnswer(self, lineToParse, lineNumber):
        rightAnswerResultObject = re.search(rightAnswerPartRegex, lineToParse)
        if rightAnswerResultObject is not None:
            notParsedRightAnswer = rightAnswerResultObject.group()
            return notParsedRightAnswer.replace(rightAnswerTextPart, '').replace(leftBracketPart, '').replace(
                rightBracketPart, '')
        print("Error parsing line. Invalid or missing correct answer on line {} ".format(lineNumber))
        return None