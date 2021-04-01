from validator import *
from questionObject import questionObject

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
        print("readFilefunction reached")
        if isValidFileName(fileName):
            print("if isValidFileName passed")
            fileToRead = open(fileName, "r",  encoding="utf8")
            amountOfReadLines = 0
            if not amountOfReadLines > self.__maxFileLineAmount:
                for line in fileToRead:
                    amountOfReadLines = amountOfReadLines + 1
                    if isValidFileLine(line):
                        print(line)
                        self.parseLine(line)
                    else:
                        "stop reading the file and send some error here"
            fileToRead.close()

        return self.__questionStructure

    # FIXME: not ready yet
    def parseLine(self, lineToParse):

        questionNumber = None
        question = None
        answerOptions = None
        rightAnswer = None

        questionNumberResultObject = re.search(questionNumberRegex, lineToParse)
        if questionNumberResultObject is not None:
            questionNumber = questionNumberResultObject.group()
            print("quetionNumber: " + questionNumber)

        print("lineToParse: " + lineToParse)
        questionResultObject = re.search(questionPartRegex, lineToParse)
        print("questionResultObject: " + str(questionResultObject))
        if questionResultObject is not None:
            questionPart = questionResultObject.group()
            print("quetionPart: " + questionPart)

        print("lineToParse: " + lineToParse)
        answerOptionsResultObject = re.search(answerOptionsPartRegex, lineToParse)
        print("answerOptionsResultObject: " + str(answerOptionsResultObject))
        if answerOptionsResultObject is not None:
            answerOptionsPart = answerOptionsResultObject.group()
            print("answerOptionsPart: " + answerOptionsPart)
        #readyQuestion = questionObject(questionNumber)
        #return readyQuestion
