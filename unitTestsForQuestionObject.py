import unittest
from questionObject import questionObject

"""
Unit test class for testing functions of question class.
"""
class QuestionObjectTestCase(unittest.TestCase):

    def setup(self):
        self.__questionObject = questionObject(1, "Test question", {'a': 'Alexander Fleming', 'b': 'something', 'c': 'test answer'}, 'a')

    def test_question_number(self):
        self.setup()
        self.assertEqual(self.__questionObject.getQuestionNumber(), 1)
        self.__questionObject.setQuestionNumber(2)
        self.assertEqual(self.__questionObject.getQuestionNumber(), 2)

    def test_question(self):
        self.setup()
        self.assertEqual(self.__questionObject.getQuestion(), "Test question")
        self.__questionObject.setQuestion("new question")
        self.assertEqual(self.__questionObject.getQuestion(), "new question")

    def test_correct_answer(self):
        self.setup()
        self.assertEqual(self.__questionObject.getRightAnswer(), "a")
        self.__questionObject.setRightAnswer("c")
        self.assertEqual(self.__questionObject.getRightAnswer(), "c")

    def test_answer_options(self):
        self.setup()
        self.assertEqual(self.__questionObject.getAnswerOptions(), {'a': 'Alexander Fleming', 'b': 'something', 'c': 'test answer'})
        self.__questionObject.setAnswerOptions({'a': 'Test 1', 'b': 'Test 2', 'c': 'Test 3'})
        self.assertEqual(self.__questionObject.getAnswerOptions(), {'a': 'Test 1', 'b': 'Test 2', 'c': 'Test 3'})

    def test_question_points(self):
        self.setup()
        self.assertEqual(self.__questionObject.getPoints(), 1)
        self.__questionObject.setPoints(2)
        self.assertEqual(self.__questionObject.getPoints(), 2)