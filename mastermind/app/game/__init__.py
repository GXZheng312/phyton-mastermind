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
        self.board.setup_board(self.amount_color, self.multi_color)
        self.board_history = []
    

    def append_history(self, blocks):
        block_row = []
        
        for n in range(len(self.board.solution)):
            block_item = board.Block(blocks[n])
            
            if blocks[n] == self.board.solution[n]: block_item.black_pin = True
            elif blocks[n] in self.board.solution: block_item.white_pin = True
            
            block_row.append(block_item)
            
        self.board_history.append(block_row)



class Board:
    def __init__(self):
        self.positions = board.MIN_POISTION
        self.solution = []
    
    def setup_board(self, amount_color, multi):
        available_colors = []

        for s in range(0, 2 if multi else 1):
            for n in range(0, amount_color):
                available_colors.append(n)

        for i in range(0, self.positions):
            self.solution.append(available_colors.pop(random.randrange(0,len(available_colors))))


class Player:
    def __init__(self, name):
        self.name = name