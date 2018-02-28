from othello.model import board
from othello.view import window


class Game(object):
    def __init__(self):
        # view
        self.window = window.Application(self)
        # model
        self.board = board.Board()
        self.board.add_observer(self.window)

        self.window.app.mainloop()

    def start(self):
        self.board.player1['state']=self.window.app.value1.get()
        self.board.player2['state']=self.window.app.value2.get()
        self.board.clear()
        self.board.set(4, 4, self.board.player1)
        self.board.set(5, 5, self.board.player1)
        self.board.set(4, 5, self.board.player2)
        self.board.set(5, 4, self.board.player2)
        self.board.notify()
        self.board.turn = 0
        self.board.now_player = None
        self.board.change_turn()

    def get_click(self, x, y):
        if 0 < self.board.turn:
            if 0 < len(self.board.able_point[y][x]):
                self.board.put(x, y)


if __name__ == '__main__':
    Game()