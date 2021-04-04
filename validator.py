import re

acceptedPlayerAmounts = ["2","3","4"]

validPlayerNameCharactersRegex = "[A-Za-z]+"
maxPlayerNameLength = 20
maxFileNameLength = 30

acceptedAnswersForFileQuesiton = ["no", "yes"]

acceptedAnswers = ["a","b","c"]
acceptedQuestionNumberRegex = "[0-9]{0,3}\. "
questionNumberRegex = "[0-9]{1,3}\."
questionPartRegex = "question: [A-Za-z0-9 ,’]+\?"
# Must have a, b and c. If only a and b has answers, c have to be also marked but answer option can be empty
answerOptionsPartRegex = "answer_options: \[a\.[A-Za-z0-9 ]+\]\[b\.[A-Za-z0-9 ]*\]\[c\.[A-Za-z0-9 ]*\]"
rightAnswerPartRegex = "correct_answer: \[[a-c]{1}\]"
#
fileLineRegex = "[0-9]{1,3}\. question: [A-Za-z0-9 ]+\? answer_options: \[a\.[A-Za-z0-9 ]+\]\[b\.[A-Za-z0-9 ]*\]\[c\.[A-Za-z0-9 ]*\] correct_answer: \[[a-c]{1}\]"
acceptedFileName = "[A-Za-z0-9_]+\.txt"

def isValidPlayerAmount(playerAmount):
    return playerAmount in acceptedPlayerAmounts

def isValidPlayerName(playerName):
    playerNameresultObject = re.search(validPlayerNameCharactersRegex, playerName)
    if playerNameresultObject is not None:
        if playerNameresultObject.group() == playerName:
            return len(playerNameresultObject.group()) <= maxPlayerNameLength
    return False

def isValidAswerForOwnQuestionFile(answer):
    return answer in acceptedAnswersForFileQuesiton

def isValidAnswer(answer):
    return answer in acceptedAnswers

def isValidFileName(fileName):
    fileNameresultObject = re.search(acceptedFileName, fileName)
    if fileNameresultObject is not None:
        print(fileNameresultObject.group())
        if fileNameresultObject.group() == fileName:
            return len(fileNameresultObject.group()) <= maxFileNameLength
    return False

# FIXME: make this return something real
def isValidFileLine(lineToValidate):
    lineResultObject = re.search(fileLineRegex, lineToValidate)
    print("lineResult: {} and lineToValidate: {}".format(lineResultObject, lineToValidate))
    if lineResultObject is not None:
        print("lineResultLenght: {} lineToValidateLenght: {}".format(len(lineResultObject.group()), len(lineToValidate.strip())))
        return len(lineResultObject.group()) == len(lineToValidate.strip())
    return False

# white listing
#black listing
#regex
