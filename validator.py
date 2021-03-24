import re

acceptedPlayerAmounts = ["2","3","4"]

validPlayerNameCharactersRegex = "[A-Za-z]+"
maxPlayerNameLength = 20

acceptedAnswersForFileQuesiton = ["no", "yes"]

acceptedAnswers = ["a","b","c","d"]
acceptedQuestionNumberRegex = "[0-9]{0,3}\. "
questionFilterRegex = "question: [A-Za-z0-9]+\?"
# Must have a, b and c. If only a and b, c have to be c. but answer option can be empty
answerPartRegex = "answer_options: a\.[A-Za-z0-9 ]+ b\.[A-Za-z0-9 ]* c\.[A-Za-z0-9 ]*"

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

# FIXME: make this return something real
def isValidFileLine(lineToValidate):
    return True

# white listing
#black listing
#regex
