from . import app, route, db, controllers

#always app
db.init_check()

# dependency injection
mastermind_game = app.game.GameObject()
cheat_enabled = False

MyData = app.MyData()
MyData.cheat_enabled = cheat_enabled 
MyData.mastermind_game = mastermind_game
