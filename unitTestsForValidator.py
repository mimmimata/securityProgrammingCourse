import unittest
import validator

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

    # FIXME!!!!
    def test_integerParameter(self):
        self.assertFalse(validator.isValidPlayerName("12"))
        #with self.assertRaisesRegex(TypeError, validator.isValidPlayerName('12')):
         #   raise TypeError('12')
        #self.assertRaises(TypeError, validator.isValidPlayerName(12))

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

if __name__ == '__main__':
    unittest.main()