import json
import os


class DataManager:

    def __init__(self, path):
        self.path = path

    def load_data_set(self,):
        try:
            with open(self.path, "r", encoding="utf8") as json_file:
                data_set = json.load(json_file)
            return data_set
        except FileNotFoundError:
            return []

    def save_data(self, data):
        current_data = self.load_data_set()
        current_data.append(data)

        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        with open(self.path, "w", encoding="utf8") as json_file:
            json.dump(current_data, json_file, indent=4)

    @staticmethod
    def load_program_state():

        state_path = DataManager("./data/program_state.json")

        state_path.load_data_set()

    @staticmethod
    def save_program_state():

        state_path = DataManager("./data/program_state.json")

        state_path.save_data()

    @staticmethod
    def update_tournaments(data):

        path = "./data/tournaments.json"
        with open(path, "w", encoding="utf8")as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)





    
    
