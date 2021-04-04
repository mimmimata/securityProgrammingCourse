from validator import *
from questionObject import questionObject

questionTextPart = "question: "
answerOptionsTextPart = "answer_options: "
rightAnswerTextPart = "correct_answer: "
leftBracketPart = "["
rightBracketPart = "]"

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
                if not amountOfReadLines > self.__maxFileLineAmount:
                    for line in fileToRead:
                        amountOfReadLines = amountOfReadLines + 1
                        if isValidFileLine(line):
                            parsedQuestionObject = self.parseLine(line, amountOfReadLines)
                            if parsedQuestionObject is not None:
                                self.__questionStructure[parsedQuestionObject.getQuestionNumber()] = parsedQuestionObject
                            else:
                                return None
                        else:
                            print("Error: stop reading the file and send some error here")
                            return None
                fileToRead.close()

                return self.__questionStructure
            except FileNotFoundError:
                print("Cannot find file!")
                return None

    def parseLine(self, lineToParse, lineNumber):

        questionNumber = None
        question = None
        # answerOptionsDict: key: a,b or c and value: answer
        answerOptions = {}
        rightAnswer = None

        questionNumberResultObject = re.search(questionNumberRegex, lineToParse)
        if questionNumberResultObject is not None:
            questionNumberAndDot = questionNumberResultObject.group()
            questionNumber = questionNumberAndDot.replace(".", '')

        questionResultObject = re.search(questionPartRegex, lineToParse)
        if questionResultObject is not None:
            notParsedQuestion = questionResultObject.group()
            question = notParsedQuestion.replace(questionTextPart, '')

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

        rightAnswerResultObject = re.search(rightAnswerPartRegex, lineToParse)
        if rightAnswerResultObject is not None:
            notParsedRightAnswer = rightAnswerResultObject.group()
            rightAnswer = notParsedRightAnswer.replace(rightAnswerTextPart, '').replace(leftBracketPart, '').replace(rightBracketPart, '')

        if questionNumber is not None and question is not None and len(answerOptions) > 0 and rightAnswer is not None:
            readyQuestion = questionObject(questionNumber, question, answerOptions, rightAnswer)
            return readyQuestion
        else:
            print("Error parsing line. Please check that line is on correct format and only allowed characters are used. Line number was: " + str(lineNumber))
            return None

