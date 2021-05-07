from validator import *
from questionObject import questionObject

questionTextPart = "question: "
answerOptionsTextPart = "answer_options: "
rightAnswerTextPart = "correct_answer: "
leftBracketPart = "["
rightBracketPart = "]"

"""
File for containing all parse functions that are needed to parse one question file line.

NOTE! We cannot force functions be private in python and there is no a check that parameters are valid
in each function because these parse functions are also used to invalid file lines to find out which
line and which part of the line has problems.
"""

def parseLine(lineToParse, lineNumber):
    # answerOptionsDict: key: a,b or c and value: answer
    answerOptions = {}

    questionNumber = parseQuestionNumber(lineToParse, lineNumber)
    if questionNumber is not None:
        question = parseQuestion(lineToParse, lineNumber)
        if question is not None:
            answerOptions = parseAswerOptions(lineToParse, answerOptions, lineNumber)
            if answerOptions is not None and len(answerOptions) > 0:
                rightAnswer = parseCorrectAnswer(lineToParse, lineNumber)
                if rightAnswer is not None:
                    readyQuestion = questionObject(questionNumber, question, answerOptions, rightAnswer)
                    return readyQuestion
    return None


def parseQuestionNumber(lineToParse, lineNumber):
    questionNumberResultObject = re.search(questionNumberRegex, lineToParse)
    if questionNumberResultObject is not None:
        questionNumberAndDot = questionNumberResultObject.group()
        return questionNumberAndDot.replace(".", '')
    print("Error parsing line. Invalid or missing question number on line {} ".format(lineNumber))
    return None


def parseQuestion(lineToParse, lineNumber):
    questionResultObject = re.search(questionPartRegex, lineToParse)
    if questionResultObject is not None:
        notParsedQuestion = questionResultObject.group()
        return notParsedQuestion.replace(questionTextPart, '')
    print("Error parsing line. Invalid or missing question on line {} ".format(lineNumber))
    return None


def parseAswerOptions(lineToParse, answerOptions, lineNumber):
    answerOptionsResultObject = re.search(answerOptionsPartRegex, lineToParse)
    if answerOptionsResultObject is not None:
        notParsedAnswerOptions = answerOptionsResultObject.group()
        answerOptionsTextPartRemoved = notParsedAnswerOptions.replace(answerOptionsTextPart, '')
        splittedAnswerOptions = answerOptionsTextPartRemoved.split(rightBracketPart)
        for answerOptionPart in splittedAnswerOptions:
            answerOption = answerOptionPart.replace(leftBracketPart, '')
            if len(answerOption) > 3:
                answerOptions[answerOption[0]] = answerOption[3:]
            elif len(answerOption) > 1:
                answerOptions[answerOption[0]] = ''
        return answerOptions
    print("Error parsing line. Invalid or missing answer options on line {} ".format(lineNumber))
    return None


def parseCorrectAnswer(lineToParse, lineNumber):
    rightAnswerResultObject = re.search(rightAnswerPartRegex, lineToParse)
    if rightAnswerResultObject is not None:
        notParsedRightAnswer = rightAnswerResultObject.group()
        return notParsedRightAnswer.replace(rightAnswerTextPart, '').replace(leftBracketPart, '').replace(
            rightBracketPart, '')
    print("Error parsing line. Invalid or missing correct answer on line {} ".format(lineNumber))
    return None