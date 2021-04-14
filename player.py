"""
Class contains information for one player
"""
class Player:
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        self.__points = 0

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getPoints(self):
        return self.__points

    def setPoints(self, points):
        # For security reason lets check that points are actually integer so that this function do not insert something
        # else in self.__points variable and that way cause some unexcepted behaviour in program and possible
        # vulnerabilities
        if isinstance(points, int):
            self.__points = points
        else:
            print("error: points must be integer type")

    def addPoints(self, points):
        # For security reason lets check that points are actually integer so that this function do not add something
        # else in self.__points variable and that way cause some unexcepted behaviour in program and possible
        # vulnerabilities
        if isinstance(points, int):
            self.__points = self.__points + points
        else:
            print("error: points must be integer type")

    def printPlayer(self):
        print("Player {}, name: {} and points {}".format(self.__number, self.__name, self.__points))