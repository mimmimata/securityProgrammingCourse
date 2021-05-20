import unittest
import validator

"""
This file contains test classes for functions inside validator file.
"""

class TestsForIsValidPlayerAmountFunction(unittest.TestCase):

    def test_correctAmount(self):
        for amount in validator.acceptedPlayerAmounts:
            self.assertTrue(validator.isValidPlayerAmount(amount))

    def test_tooSmallAmount(self):
        self.assertFalse(validator.isValidPlayerAmount('1'))

    def test_tooBigAmount(self):
        self.assertFalse(validator.isValidPlayerAmount('5'))

    def test_floatParameter(self):
        self.assertFalse(validator.isValidPlayerAmount(2.2))

    def test_integerParameter(self):
        self.assertFalse(validator.isValidPlayerAmount(2))

    def test_incorrectStringParameter(self):
        self.assertFalse(validator.isValidPlayerAmount("Test€$£"))

class TestsForIsValidPlayerNameFunction(unittest.TestCase):

    def test_correctName(self):
        self.assertTrue(validator.isValidPlayerName("CorrectTestName"))

    def test_tooLongName(self):
        self.assertFalse(validator.isValidPlayerName("TestNameThatIsWayTooLongForThisProgram"))

    def test_spaceInName(self):
        self.assertFalse(validator.isValidPlayerName("Test Name"))

    def test_numberParameter(self):
        self.assertFalse(validator.isValidPlayerName("12"))

    def test_incorrectCharacters(self):
        self.assertFalse(validator.isValidPlayerName("3rwecs7%6f"))


class TestsForIsValidAnswerForOwnQuestionFileFunction(unittest.TestCase):

    def test_withCorrectAnswers(self):
        for answer in validator.acceptedAnswersForFileQuestion:
            self.assertTrue(validator.isValidAswerForOwnQuestionFile(answer))

    def test_withIncorrectAnswers(self):
        self.assertFalse(validator.isValidAswerForOwnQuestionFile("random answer"))

    def test_withIncorrectParameterType(self):
        self.assertFalse(validator.isValidAswerForOwnQuestionFile(324))

class TestsForIsValidAnswerFunction(unittest.TestCase):

    def test_withCorrectAnswers(self):
        for answer in validator.acceptedAnswers:
            self.assertTrue(validator.isValidAnswer(answer))

    def test_withIncorrectAnswers(self):
        self.assertFalse(validator.isValidAnswer("r%"))

    def test_withIncorrectParameterType(self):
        self.assertFalse(validator.isValidAnswer(324))


class TestsForIsValidFileNameFunction(unittest.TestCase):
    def test_withCorrectFileName(self):
        self.assertTrue(validator.isValidFileName("correctTestName.txt"))

    def test_withCorrectFileName2(self):
        self.assertTrue(validator.isValidFileName("correct_test_file_2.txt"))

    def test_withSpaces(self):
        self.assertFalse(validator.isValidFileName("test file 2.txt"))

    def test_withoutFileFormat(self):
        self.assertFalse(validator.isValidFileName("testName"))

    def test_withWrongFileFormat(self):
        self.assertFalse(validator.isValidFileName("testName.svg"))

    def test_withSomeInvalidCharacters(self):
        self.assertFalse(validator.isValidFileName("#¤23423&#^^"))


class TestsForIsValidFileLineFunction(unittest.TestCase):
    def test_withCorrectLine(self):
        self.assertTrue(validator.isValidFileLine(
            "1. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.] correct_answer: [a]"))

    def test_withCorrectLine2(self):
        self.assertTrue(validator.isValidFileLine(
            "1. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b. some one else ][c. some one else] correct_answer: [b]"))

    def test_withoutLineQuestionNumber(self):
        self.assertFalse(validator.isValidFileLine(
            "question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b. some one else ][c. some one else] correct_answer: [b]"))

    def test_withoutAnswerOptions(self):
        self.assertFalse(validator.isValidFileLine(
            "1. question: Who discovered penicillin? correct_answer: [b]"))

    def test_withoutCorrectAnswer(self):
        self.assertFalse(validator.isValidFileLine(
            "1. question: Who discovered penicillin? answer_options: [a. Alexander Fleming][b.][c.]"))

    def test_randomLineContent(self):
        self.assertFalse(validator.isValidFileLine("hello 3%#//&%/randomrandom___rrandom"))

if __name__ == '__main__':
    # This will run all tests for inside this unitTestsForValidator file.
    unittest.main()