import mastermind
from flask import render_template


def index():
    all_games = []
    for player in mastermind.db.get_all_players():
        amount_games = len(player['games'])
        for game in player['games']:
            game["player"] = player['name']
            game["amount_games"] = amount_games
            all_games.append(game)
    all_games.sort(key=lambda game: game.get('finished_turn'))
    mastermind.my_data.all_games = all_games

    return render_template('leaderboard.html', data=mastermind.my_data)
