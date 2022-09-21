class Settings():
    def __init__(self) :
        self.title="Tic Tac Toe"
        self.screen_size="530x520"
        self.bgcolor="tan"
        self.title_font = ("arial",50,"bold")
        self.text_font = ("arial",30)
       


class Player():
    def __init__(self,color,char):
        self.win=0
        self.tied=0
        self.total=0
        self.color=color
        self.char= char

class Game():
    def __init__(self,turn,color):
        self.turn=turn
        self.turn_color=color
        self.count=0
        self.game_mode="1p"