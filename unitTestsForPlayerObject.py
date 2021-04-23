import unittest
from player import Player

class PlayerObjectTestCase(unittest.TestCase):

    def setup(self):
        self.__player = Player(1, "testName")

    def test_player_name(self):
        self.setup()
        self.assertEqual(self.__player.getName(), "testName")

    def test_player_number(self):
        self.setup()
        self.assertEqual(self.__player.getName(), "testName")

    def test_set_points(self):
        self.setup()
        self.assertEqual(self.__player.getPoints(), 0)
        self.__player.setPoints(2)
        self.assertEqual(self.__player.getPoints(), 2)
        self.__player.setPoints(3)
        self.assertEqual(self.__player.getPoints(), 3)

    def test_add_points(self):
        self.setup()
        self.assertEqual(self.__player.getPoints(), 0)
        self.__player.addPoints(2)
        self.assertEqual(self.__player.getPoints(), 2)
        self.__player.addPoints(3)
        self.assertEqual(self.__player.getPoints(), 5)

