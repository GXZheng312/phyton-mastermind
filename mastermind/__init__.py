from . import app, route, db, controllers

db.init_check()
mastermind_game = app.game.GameObject()
CHEAT_ENABLED = False