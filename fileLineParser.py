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

"""
Parses line from file and return ready question object.
@:parameter lineToParse line which parsing is made
@:parameter lineNumber number of that line from file where line is got.
@:return questionObject containing all necessary information if it can be created, None otherwise.
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

"""
Parses question number from file line and returns it.
@:parameter lineToParse line which parsing is made.
@:parameter lineNumber number of that line from file where line is got.
@:return question number if it is found, None otherwise.
"""
def parseQuestionNumber(lineToParse, lineNumber):
    questionNumberResultObject = re.search(questionNumberRegex, lineToParse)
    if questionNumberResultObject is not None:
        questionNumberAndDot = questionNumberResultObject.group()
        return questionNumberAndDot.replace(".", '')
    print("Error parsing line. Invalid or missing question number on line {} ".format(lineNumber))
    return None

"""
Parses question from file line and returns it.
@:parameter lineToParse line which parsing is made.
@:parameter lineNumber number of that line from file where line is got.
@:return question if it is found, None otherwise.
"""
def parseQuestion(lineToParse, lineNumber):
    questionResultObject = re.search(questionPartRegex, lineToParse)
    if questionResultObject is not None:
        notParsedQuestion = questionResultObject.group()
        return notParsedQuestion.replace(questionTextPart, '')
    print("Error parsing line. Invalid or missing question on line {} ".format(lineNumber))
    return None

"""
Parses answer options from file line and returns them.
@:parameter lineToParse line which parsing is made.
@:parameter answerOptions dict where answerOptions are added.
@:parameter lineNumber number of that line from file where line is got.
@:return answerOptions as a dict if it can be created, None otherwise.
"""
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

"""
Parses correct answer from file line and returns it.
@:parameter lineToParse line which parsing is made
@:parameter lineNumber number of that line from file where line is got.
@:return correct answer if it is found, None otherwise.
"""
def parseCorrectAnswer(lineToParse, lineNumber):
    rightAnswerResultObject = re.search(rightAnswerPartRegex, lineToParse)
    if rightAnswerResultObject is not None:
        notParsedRightAnswer = rightAnswerResultObject.group()
        return notParsedRightAnswer.replace(rightAnswerTextPart, '').replace(leftBracketPart, '').replace(
            rightBracketPart, '')
    print("Error parsing line. Invalid or missing correct answer on line {} ".format(lineNumber))
    return None