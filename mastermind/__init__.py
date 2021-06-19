from . import app, route, db, controllers

#always app
db.init_check()

# dependency injection
mastermind_game = app.game.GameObject()

my_data = app.MyData()
my_data.cheat_enabled = False 
my_data.mastermind_game = mastermind_game
