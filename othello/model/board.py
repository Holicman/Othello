from othello.model import computer

class Board(object):
    def __init__(self):
        self.observer = None
        self.info = ''
        self.cells = [['green' for i in range(10)] for j in range(10)]
        self.able_point = [[[] for i in range(10)] for j in range(10)]
        self.able_point_set = []
        self.ables = {'player1':0,'player2':0}
        self.player1 = {'state': 'Human',
                        'color': 'white',
                        'o_color': 'black',
                        'name': 'player1',
                        'num': 0}
        self.player2 = {'state': 'Human',
                        'color': 'black',
                        'o_color': 'white',
                        'name': 'player2',
                        'num': 0}
        self.com1 = computer.Computer()
        self.com2 = computer.Computer()
        self.turn = -1
        self.now_player = None

    def add_observer(self, observer):
        self.observer = observer

    def clear(self):
        self.cells = [['green' for i in range(10)] for j in range(10)]

    def notify(self):
        self.observer.app.update_board(self)

    def set(self, x, y, player):
        self.cells[y][x] = player['color']
        self.notify()

    def change_turn(self):
        if self.now_player == self.player1:
            self.now_player = self.player2

            if self.now_player['state'] == 'Human':
                pass
            elif self.now_player['state'] == 'Computer':
                x, y = self.com2.randomAI(self)
                self.put(x, y)

        else:
            self.now_player = self.player1

            if self.now_player['state'] == 'Human':
                pass
            elif self.now_player['state'] == 'Computer':
                x, y = self.com1.randomAI(self)
                self.put(x, y)

        self.turn = self.turn + 1
        self.board_check()

        if self.ables['player1'] == 0 and self.ables['player2'] == 0:
            self.finish()

        elif self.ables[self.now_player['name']] == 0:
            self.change_turn()

        self.notify()

    def reverse(self,x,y):
        if self.cells[y][x] == 'black':
            self.cells[y][x] = 'white'
        elif self.cells[y][x] == 'white':
            self.cells[y][x] = 'black'

    # 盤面サーチ
    def board_check(self):
        self.player1['num'] = 0
        self.player2['num'] = 0
        able_num = 0
        self.able_point_set = []
        for y in range(1,9):
            for x in range(1,9):
                able_revers = []
                temp_able_revers = []

                if self.cells[y][x] == 'green':
                    # x+1方向
                    temp_able_revers = []
                    temp_x = x + 1
                    temp_y = y
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x + 1
                        temp_y = temp_y
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # x-1方向
                    temp_able_revers = []
                    temp_x = x - 1
                    temp_y = y
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x - 1
                        temp_y = temp_y
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # y+1方向
                    temp_able_revers = []
                    temp_x = x
                    temp_y = y + 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x
                        temp_y = temp_y + 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # y-1方向
                    temp_able_revers = []
                    temp_x = x
                    temp_y = y - 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x
                        temp_y = temp_y - 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # x+1,y+1方向
                    temp_able_revers = []
                    temp_x = x + 1
                    temp_y = y + 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x + 1
                        temp_y = temp_y + 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # x+1,y-1方向
                    temp_able_revers = []
                    temp_x = x + 1
                    temp_y = y - 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x + 1
                        temp_y = temp_y - 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # x-1,y+1方向
                    temp_able_revers = []
                    temp_x = x - 1
                    temp_y = y + 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x - 1
                        temp_y = temp_y + 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                    # x-1,y-1方向
                    temp_able_revers = []
                    temp_x = x - 1
                    temp_y = y - 1
                    while self.cells[temp_y][temp_x] == self.now_player['o_color']:
                        temp_able_revers.append((temp_x, temp_y))
                        temp_x = temp_x - 1
                        temp_y = temp_y - 1
                    if self.cells[temp_y][temp_x] == self.now_player['color']:
                        able_revers.extend(temp_able_revers)

                self.able_point[y][x] = able_revers
                if 0 < len(able_revers):
                    self.able_point_set.append((x-1,y-1))

                if self.cells[y][x] == 'white': self.player1['num'] += 1
                if self.cells[y][x] == 'black': self.player2['num'] += 1

                able_num += len(able_revers)
        self.ables[self.now_player['name']] = able_num

    def put(self,x,y):
        if 0 < len(self.able_point[y][x]):
            for point_x, point_y in self.able_point[y][x]:
                self.reverse(point_x, point_y)

            self.cells[y][x] = self.now_player['color']
            self.board_check()
            self.info = '{}:{}'.format(self.player1['num'], self.player2['num'])
            self.notify()
            self.change_turn()


    def finish(self):
        if self.player1['num'] > self.player2['num']:
            message = ('Win','Lose')
        elif self.player1['num'] < self.player2['num']:
            message = ('Lose','Win')
        else:
            message = ('Draw','Draw')
        self.info = '{}-{}:{}-{}'.format(message[0],self.player1['num'], self.player2['num'],message[1])
        self.notify()