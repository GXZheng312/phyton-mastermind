import json
import os

JSON_FILE_PATH = 'mastermind/resources/data.json'
DEFAULT_DATA = { "players": [
    {
        "name": "guest",
        "games": [{
            "finished_turn": 10,
            "cheated": False,
            "datetime": "17-6-2021T15:00",
        },
        ]
     }
]}


def init_check():
    if os.path.isfile(JSON_FILE_PATH) is False:
        print("File does not exist, create new one")
        with open(JSON_FILE_PATH, 'w') as outfile:
            json.dump(DEFAULT_DATA, outfile)
        outfile.close()
        print("new file created")


def get_player(name):
    if name is not None:
        with open(JSON_FILE_PATH) as file:
            data = json.load(file)
            return next((player_data for player_data in data["players"] if player_data['name'] == name), None)


def save_player(name, finished_turn, cheated):
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, "r+") as file:
            old_data = json.load(file)
            data = {
                    "name": name,
                    "games": [{
                        "finished_turn": finished_turn,
                        "cheated": cheated,
                    },
                ]
            }
            old_data["players"].append(data)
            file.seek(0)
            json.dump(old_data, file)


save_player("ody", 25, True)
save_player("jacky", 45, False)
save_player("test", 3, True)
