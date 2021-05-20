import re
# -*- coding: utf-8 -*-

"""
This file contains validation functions that can be used validate for example validate user inputs. 
These functions are collected in one file to make program structure more clear.
"""

# SECURE_PROGRAMMING_SOLUTION: Allowed character lists.
acceptedPlayerAmounts = ["2","3","4"]
acceptedAnswersForFileQuestion = ["no", "yes"]
acceptedAnswers = ["a","b","c","s"]

# SECURE_PROGRAMMING_SOLUTION: Maximum character amounts.
maxPlayerNameLength = 20
maxFileNameLength = 30
maxFileLineAmount = 300

# SECURE_PROGRAMMING_SOLUTION: Using regexs for making sure that only allowed character in right order can be
# inputted to the program.
validPlayerNameCharactersRegex = "[A-Za-z]+"
acceptedQuestionNumberRegex = "[0-9]{0,3}\. "
questionNumberRegex = "[0-9]{1,3}\."
questionPartRegex = "question: [A-Za-z0-9 ,’]+\?"
# Must have a, b and c. If only a and b has answers, c have to be also marked but answer option can be empty
answerOptionsPartRegex = "answer_options: \[a\.[A-Za-z0-9 ]+\]\[b\.[A-Za-z0-9 ]*\]\[c\.[A-Za-z0-9 ]*\]"
rightAnswerPartRegex = "correct_answer: \[[a-c]{1}\]"
fileLineRegex = "[0-9]{1,3}\. question: [A-Za-z0-9 ,’]+\? answer_options: \[a\.[A-Za-z0-9 ]+\]\[b\.[A-Za-z0-9 ]*\]\[c\.[A-Za-z0-9 ]*\] correct_answer: \[[a-c]{1}\]"
acceptedFileName = "[A-Za-z0-9_]+\.txt"

def isValidPlayerAmount(playerAmount):
    return playerAmount in acceptedPlayerAmounts

def isValidPlayerName(playerName):
    # SECURE_PROGRAMMING_SOLUTION: Using specific regex to find only wanted part from line.
    playerNameresultObject = re.search(validPlayerNameCharactersRegex, playerName)
    # SECURE_PROGRAMMING_SOLUTION: result object needs to be check that it is not None.
    if playerNameresultObject is not None:
        if playerNameresultObject.group() == playerName:
            return len(playerNameresultObject.group()) <= maxPlayerNameLength
    return False

def isValidAswerForOwnQuestionFile(answer):
    return answer in acceptedAnswersForFileQuestion

def isValidAnswer(answer):
    return answer in acceptedAnswers

def isValidFileName(fileName):
    # SECURE_PROGRAMMING_SOLUTION: Using specific regex to find only wanted part from line.
    fileNameresultObject = re.search(acceptedFileName, fileName)
    # SECURE_PROGRAMMING_SOLUTION: result object needs to be check that it is not None.
    if fileNameresultObject is not None:
        if fileNameresultObject.group() == fileName:
            return len(fileNameresultObject.group()) <= maxFileNameLength
    return False

def isValidFileLine(lineToValidate):
    # SECURE_PROGRAMMING_SOLUTION: Using specific regex to find only wanted part from line.
    lineResultObject = re.search(fileLineRegex, lineToValidate)
    # SECURE_PROGRAMMING_SOLUTION: result object needs to be check that it is not None.
    if lineResultObject is not None:
        return len(lineResultObject.group()) == len(lineToValidate.strip())
    return False
