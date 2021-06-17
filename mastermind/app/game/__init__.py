# from mastermind.app.module_one.example import ExampleClass
# rom . import 

class GameObject:
    def __init__(self, player):
        self.player = player
        self.board = Board()

    def allowMultiColor(self, allow = True):
        self.isMultiColorOn = allow


class Board:
    def __init__(self):
        self.row = None

class Player:
    def __init__(self, name):
        self.name = name