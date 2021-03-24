from validator import *

class FileReader:

    def __init__(self):
        self.__fileToRead = None
        self.__questionStructure = {}

    def addFileToRead(self, fileName):
        if isValidFileName(fileName):
            self.__fileToRead = fileName

    def readFile(self, fileName):
        print("readFilefunction reached")
        if isValidFileName(fileName):
            print("if isValidFileName passed")
            fileToRead = open(fileName, "r",  encoding="utf8")
            for line in fileToRead:
                print(line)
            fileToRead.close()

    def parseLine(self, lineToParse):
        try:
            lineString = str(lineToParse)
        except ValueError:
            print("Line cannot be cast as a string")
            return