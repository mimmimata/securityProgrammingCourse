import unittest
from fileLineParser import *
from questionObject import questionObject

"""
Unit test class for testing file line parsing functions on fileLineParser.
"""
class PlayerObjectTestCase(unittest.TestCase):

    def setup(self):
        self.__correctLineToParse = "3. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.__lineNumber = 3

    def test_parse_question_number(self):
        self.setup()
        self.assertEqual(parseQuestionNumber(self.__correctLineToParse, self.__lineNumber), "3")
        questionWithoutNumber = "question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.assertEqual(parseQuestionNumber(questionWithoutNumber, self.__lineNumber), None)

    def test_parse_question(self):
        self.setup()
        self.assertEqual(parseQuestion(self.__correctLineToParse, self.__lineNumber), "Who discovered penicillin?")
        questionWithoutQuestionTag = "3. Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.assertEqual(parseQuestion(questionWithoutQuestionTag, self.__lineNumber), None)
        questionTagWithoutQuestion = "3. question: answer_options: [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.assertEqual(parseQuestion(questionTagWithoutQuestion, self.__lineNumber), None)

    def test_parse_answer_options(self):
        self.setup()
        self.assertEqual(parseAswerOptions(self.__correctLineToParse, {}, self.__lineNumber), {"a": "Alexander Fleming", "b": "", "c": ""})
        answerOptionsWithoutTag = "3. question: Who discovered penicillin? [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.assertEqual(parseAswerOptions(answerOptionsWithoutTag, {}, self.__lineNumber), None)
        answerOptionsWithoutOneOption = "3. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][.][c.] correct_answer: [a]"
        self.assertEqual(parseAswerOptions(answerOptionsWithoutOneOption, {}, self.__lineNumber), None)
        answerOptionsWithoutAnswerOptions = "3. question: Who discovered penicillin? answer_options: correct_answer: [a]"
        self.assertEqual(parseAswerOptions(answerOptionsWithoutAnswerOptions, {}, self.__lineNumber), None)

    def test_parse_correct_answer(self):
        self.setup()
        self.assertEqual(parseCorrectAnswer(self.__correctLineToParse, self.__lineNumber), "a")
        correctAnswerWithoutAnswer = "3. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] correct_answer: []"
        self.assertEqual(parseCorrectAnswer(correctAnswerWithoutAnswer, self.__lineNumber), None)
        correctAnswerWithoutAnswerTag = "3. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] [a]"
        self.assertEqual(parseCorrectAnswer(correctAnswerWithoutAnswerTag, self.__lineNumber), None)

    # This function uses all above functions which are tested before so that is why in here is only tested that
    # one working questionObject is returned when file line is correct and one case when line is not correct and None
    # is returned.
    def test_parse_line(self):
        self.setup()
        testQuestionObject = questionObject("3", "Who discovered penicillin?", {"a": "Alexander Fleming", "b": "", "c": ""},"a")
        parsedQuestionObject = parseLine(self.__correctLineToParse, self.__lineNumber)

        self.assertEqual(testQuestionObject.getQuestionNumber(), parsedQuestionObject.getQuestionNumber())
        self.assertEqual(testQuestionObject.getQuestion(), parsedQuestionObject.getQuestion())
        self.assertEqual(testQuestionObject.getAnswerOptions(), parsedQuestionObject.getAnswerOptions())
        self.assertEqual(testQuestionObject.getRightAnswer(), parsedQuestionObject.getRightAnswer())

        brokenFileLine = "3. question: Who discovered penicillin? answer_options: #¤¤#TFERGEFDV [a. Alexander Fleming][b.][c.] correct_answer: [a]"
        self.assertEqual(parseLine(brokenFileLine, self.__lineNumber), None)