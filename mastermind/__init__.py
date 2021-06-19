from . import app, route, db, controllers

CHEAT_ENABLED = False
db.init_check()
mastermind_game = app.game.GameObject()