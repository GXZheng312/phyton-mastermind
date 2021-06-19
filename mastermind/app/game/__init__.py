# from mastermind.app.module_one.example import ExampleClass
from . import board

MAX_COLORS = 10
MIN_COLORS = 6

class GameObject:
    def __init__(self):
        self.player = None
        self.board = Board()
        self.multi_color = False
        self.amount_color = MIN_COLORS
        self.board_history = []

    def set_player(self, name):
        self.player = Player(name)


class Board:
    def __init__(self):
        self.positions = board.MIN_POISTION
        self.answer = []
    
    def setup_board(self):
        self.answer



class Player:
    def __init__(self, name):
        self.name = name