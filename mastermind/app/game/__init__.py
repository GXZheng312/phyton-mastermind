# from mastermind.app.module_one.example import ExampleClass
from . import board
import random

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
        self.new_game()

    def new_game(self):
        self.board.setup_board(self.amount_color)
        self.board_history = []


class Board:
    def __init__(self):
        self.positions = board.MIN_POISTION
        self.answer = []
    
    def setup_board(self, amount_color):
        for i in range(0, self.positions):
            n = random.randint(0, amount_color)
            self.answer.append(n)

    



class Player:
    def __init__(self, name):
        self.name = name