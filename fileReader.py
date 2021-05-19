from validator import *
from fileLineParser import parseLine
"""
Class for containing all functionality what is needed to read question file.
"""
class FileReader:

    def __init__(self):
        # key: question number, value: questionObject
        self.__questionStructure = {}


    def readFile(self, fileName):
        if isValidFileName(fileName):
            try:
                fileToRead = open(fileName, "r",  encoding="utf8")
                amountOfReadLines = 0
                if amountOfReadLines <= maxFileLineAmount:
                    for line in fileToRead:
                        amountOfReadLines = amountOfReadLines + 1
                        if isValidFileLine(line):
                            parsedQuestionObject = parseLine(line, amountOfReadLines)
                            if parsedQuestionObject is not None:
                                self.__questionStructure[parsedQuestionObject.getQuestionNumber()] = parsedQuestionObject
                            else:
                                return None
                        else:
                            # parseLine is called even for not valid file line so user gets an accurate error message
                            # which tells where the problem is.
                            parseLine(line, amountOfReadLines)
                            return None
                else:
                    print("Error parsing line. There is too many lines in file. Allowed line amount is: {}".format(
                        maxFileLineAmount))
                fileToRead.close()

                return self.__questionStructure
            except FileNotFoundError:
                print("Cannot find file!")
                return None

