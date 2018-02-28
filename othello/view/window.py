import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self,controller=None):
        self.root = tk.Tk()
        self.app = Window(self.root, controller=controller)


#マスターフレーム
class Window(tk.Frame):
    cells = 8
    cell_size = 80
    margin_board = 20
    margin_oval = 10
    canvas_size = cell_size * cells + margin_board * 2

    def __init__(self, master=None, controller=None):
        self.controller = controller

        super().__init__(master)
        self.master.title('Othello')
        self.setting_window = None
        self.value1 = tk.StringVar()
        self.value2 = tk.StringVar()
        # デフォルトユーザー
        self.value1.set('Human')
        self.value2.set('Human')

        # メニュー
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.menu_bar.add_command(label='Game Start',command=lambda: self.controller.start())
        self.menu_bar.add_command(label='Settings',command=lambda: self.setting())

        #プレイヤーラベル
        self.label_player_1 = tk.Label(self.master, text='{}：〇')
        self.label_player_2 = tk.Label(self.master, text='●：{}')
        self.label_player_1.grid(row=0, column=0)
        self.label_player_2.grid(row=0, column=2)

        #indoラベル
        self.label_info = tk.Label(self.master, text='please start a game')
        self.label_info.grid(row=0, column=1)

        #ボード
        self.board = tk.Canvas(self.master, bg='green', width=self.canvas_size, height=self.canvas_size)
        self.create_board()
        self.board.bind('<Button-1>', self.clicked)

    def clicked(self, event):
        x = (event.x - self.margin_board)//self.cell_size + 1
        y = (event.y - self.margin_board)//self.cell_size + 1
        self.controller.get_click(x, y)

    def create_board(self):
        for i in range(self.cells + 1):
            x1 = self.margin_board + self.cell_size * i
            y1 = self.margin_board
            y2 = self.margin_board + self.cell_size * self.cells + 1

            self.board.create_line(x1, y1, x1, y2)

            x1 = self.margin_board
            x2 = self.margin_board + self.cell_size * self.cells + 1
            y1 = self.margin_board + self.cell_size * i
            self.board.create_line(x1, y1, x2, y1)
        self.board.grid(row=1,column=0,columnspan=3)

    def update_board(self, board_info):
        for y in range(8):
            for x in range(8):
                x1 = x * self.cell_size + self.margin_board + self.margin_oval
                y1 = y * self.cell_size + self.margin_board + self.margin_oval
                x2 = (x + 1) * self.cell_size + self.margin_board - self.margin_oval
                y2 = (y + 1) * self.cell_size + self.margin_board - self.margin_oval
                self.board.create_oval(x1, y1, x2, y2, fill=board_info.cells[y+1][x+1], width=0)
        for p in board_info.able_point_set:
            x,y = p
            x1 = x * self.cell_size + self.margin_board + self.margin_oval*2
            y1 = y * self.cell_size + self.margin_board + self.margin_oval*2
            x2 = (x + 1) * self.cell_size + self.margin_board - self.margin_oval*2
            y2 = (y + 1) * self.cell_size + self.margin_board - self.margin_oval*2
            self.board.create_oval(x1, y1, x2, y2, fill='lime', width=0)

        player1 = board_info.player1['state']
        player2 = board_info.player2['state']
        self.label_player_1.configure(text='{}：〇'.format(board_info.player1['state']))
        self.label_player_2.configure(text='●：{}'.format(board_info.player2['state']))
        self.label_info.configure(text=board_info.info)

    def setting(self):
        self.setting_window = tk.Toplevel()
        self.setting_window.transient()
        self.setting_window.grab_set()
        self.setting_window.focus_set()

        setting_label_1 = tk.Label(self.setting_window, text='Player1:')
        setting_label_2 = tk.Label(self.setting_window, text='Player2:')
        setting_label_1.grid(row=0, column=0)
        setting_label_2.grid(row=1, column=0)

        players = ('Human', 'Computer')

        setting_player_1 = ttk.Combobox(self.setting_window, textvariable=self.value1)
        setting_player_2 = ttk.Combobox(self.setting_window, textvariable=self.value2)
        setting_player_1['values'] = players
        setting_player_2['values'] = players
        setting_player_1.set('Human')
        setting_player_2.set('Human')
        setting_player_1.grid(row=0, column=1)
        setting_player_2.grid(row=1, column=1)
        setting_button_1 = tk.Button(self.setting_window, text='close', command=lambda: self.setting_window.destroy())
        setting_button_1.grid(row=2, column=2,columnspan=2)



if __name__ == '__main__':
    Application()