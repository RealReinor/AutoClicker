import json
import keyboard

class SettingsManager:
    def __init__(self):
        with open("settings.json") as f:
            settings_json = json.load(f)
            self.start_button = settings_json["start_button"]
            self.quit_button = settings_json["quit_button"]
            self.settings_button = settings_json["settings_button"]
            self.clicking_button = settings_json["clicking_button"]


    def record_new_start_button_key(self):
        while True:
            new_key = keyboard.read_event(suppress=True)
            if new_key.event_type == 'up':
                with open("settings.json", 'r+') as f:
                    settings_json = json.load(f)
                    settings_json["start_button"] = new_key.name
                    f.seek(0)
                    json.dump(settings_json,f, indent=4)
                    f.truncate()
                    self.start_button = settings_json['start_button']
                break