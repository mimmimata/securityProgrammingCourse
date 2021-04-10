import unittest
import validator

class TestsForisValidPlayerAmountFunction(unittest.TestCase):

    def test_isValidPlayerAmountWithCorrectAmount(self):
        self.assertTrue(validator.isValidPlayerAmount('2'))

    def test_isValidPlayerAmountWithTooSmallAmount(self):
        self.assertFalse(validator.isValidPlayerAmount('1'))

    def test_isValidPlayerAmountWithTooBigAmount(self):
        self.assertFalse(validator.isValidPlayerAmount('5'))

    def test_isValidPlayerAmountWithFloat(self):
        self.assertFalse(validator.isValidPlayerAmount(2.2))

    def test_isValidPlayerAmountWithInteger(self):
        self.assertFalse(validator.isValidPlayerAmount(2))

    def test_isValidPlayerAmountWithIncorrectString(self):
        self.assertFalse(validator.isValidPlayerAmount("Test€$£"))

if __name__ == '__main__':
    unittest.main()