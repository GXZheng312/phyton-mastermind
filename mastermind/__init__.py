from . import app, route, db, controllers

#always app
db.init_check()

# dependency injection
MyData = app.MyData()
MyData.cheat_enabled = False 
MyData.mastermind_game = app.game.GameObject()
