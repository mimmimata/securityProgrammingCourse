from validator import *
from fileLineParser import parseLine

"""
Class for containing all functionality what is needed to read question file.
"""
class FileReader:

    def __init__(self):
        # key: question number, value: questionObject
        self.__questionStructure = {}

    """
    Reads the question file and creates question structure from it.
    @:parameter fileName name of the question file
    @:return ready question structure as a dict or None if file cannot be read
    """
    def readFile(self, fileName):
        # SECURE_PROGRAMMING_SOLUTION: checking that file name is valid before reading it.
        if isValidFileName(fileName):
            try:
                fileToRead = open(fileName, "r",  encoding="utf8")
                amountOfReadLines = 0

                # SECURE_PROGRAMMING_SOLUTION: checking that there is no more than maximum allowed lines in file.
                if amountOfReadLines <= maxFileLineAmount:
                    for line in fileToRead:
                        amountOfReadLines = amountOfReadLines + 1

                        # SECURE_PROGRAMMING_SOLUTION: Every line needs to be check that they are valid before parsing them.
                        if isValidFileLine(line):
                            parsedQuestionObject = parseLine(line, amountOfReadLines)

                            # SECURE_PROGRAMMING_SOLUTION: Do not add question object to question map if it is None
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
                    # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
                    print("Error parsing line. There is too many lines in file. Allowed line amount is: {}".format(
                        maxFileLineAmount))
                fileToRead.close()

                return self.__questionStructure
            except FileNotFoundError:
                # SECURE_PROGRAMMING_SOLUTION: Error handling and informing user.
                print("Cannot find file!")
                return None

