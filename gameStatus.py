class GameState:

    def __init__(self):
        INITIAL_STATE = "initial"
        RUNNING_STATE = "running"
        GAME_OVER_STATE = "game over"
        self.__allowedGameStates = [INITIAL_STATE, RUNNING_STATE, GAME_OVER_STATE]
        self.__gameState = INITIAL_STATE

    def getGameState(self):
        return self.__gameState


    def setGameState(self, newState):
        # Making sure that newState is actually one of the allowed states of the program and nothing else
        # so that program works correctly
        if self.__allowedGameStates.contains(newState):
            self.__gameState = newState
        else:
            print("Error: Cannot change game state to illegal state")


