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

def isValidFileName(fileName):
    resultObject = re.search(acceptedFileName, fileName)
    if resultObject is not None:
        print(resultObject.group())
        if resultObject.group() == fileName:
            return len(resultObject.group()) <= maxFileNameLength
    return False

# FIXME: make this return something real
def isValidFileLine(lineToValidate):
    return True

# white listing
#black listing
#regex
