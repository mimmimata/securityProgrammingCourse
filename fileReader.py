from validator import *

class FileReader:

    def __init__(self):
        self.__fileToRead = None
        # key: question number, value: question as string
        self.__questionStructure = {}
        # key: question number, value: list of correct answers
        self.__answerStructure = {}
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
                    else:
                        "stop reading the file and send some error here"
            fileToRead.close()

    # FIXME: not ready yet
    def parseLine(self, lineToParse):
        try:
            lineString = str(lineToParse)
        except ValueError:
            print("Line cannot be cast as a string")
            return