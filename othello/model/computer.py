import random

class Computer:
    def __init__(self):
        pass

    def randomAI(self, board):
        board.board_check()
        number = len(board.able_point_set)
        if number == 0:
            return 0, 0
        x, y = board.able_point_set[random.randrange(number)]
        print(x,y)
        return x+1, y+1