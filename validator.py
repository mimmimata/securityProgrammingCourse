import re

acceptedPlayerAmounts = ["2","3","4"]

validPlayerNameCharactersRegex = "[A-Za-z]+"
maxPlayerNameLength = 20

acceptedAnswersForFileQuesiton = ["no", "yes"]

acceptedAnswers = ["a","b","c","d"]

def isValidPlayerAmount(playerAmount):
    return playerAmount in acceptedPlayerAmounts

def isValidPlayerName(playerName):
    resultObject = re.search(validPlayerNameCharactersRegex, playerName)
    if resultObject is not None:
        print(resultObject.group())
        if resultObject.group() == playerName:
            return len(resultObject.group()) <= maxPlayerNameLength
    return False

def isValidAswerForOwnQuestionFile(answer):
    return answer in acceptedAnswersForFileQuesiton

def isValidAnswer(answer):
    return answer in acceptedAnswers

# FIXME: make this return something real
def isValidFileName(fileName):
    return True

# white listing
#black listing
#regex
