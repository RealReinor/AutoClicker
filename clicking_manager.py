import pyautogui
import keyboard
import json
import threading


class ClickingManager:
    def __init__(self):
        with open("settings.json") as s:
            settings_json = json.load(s)
            self.start_button = settings_json["start_button"]
            self.quit_button = settings_json["quit_button"]
            self.settings_button = settings_json["settings_button"]
            self.clicking_button = settings_json["clicking_button"]
        self.auto_clicking = False
        self.click_thread = None
        self.listener_thread = None
        self.active = True
        self.event = threading.Event()
        pyautogui.PAUSE = 0.01

    def auto_click(self):
        while self.auto_clicking:
            pyautogui.click()

    def start_auto_click(self):
        if not self.auto_clicking:
            self.auto_clicking = True
            self.click_thread = threading.Thread(target=self.auto_click)
            self.click_thread.start()

    def stop_auto_click(self):
        if self.auto_clicking:
            self.auto_clicking = False
            if self.click_thread is not None:
                self.click_thread.join()

    def on_key_event(self, event):
        if event.event_type == "up" and event.name == self.start_button:
            if self.auto_clicking:
                self.stop_auto_click()
            else:
                self.start_auto_click()

    def read_key_event(self):
        def key_listener():
            keyboard.hook(self.on_key_event)
            self.event.wait()

        if self.listener_thread is None or not self.listener_thread.is_alive():
            self.listener_thread = threading.Thread(target=key_listener)
            self.listener_thread.start()

    def stop_key_listener(self):
        self.event.set()
        keyboard.unhook_all()
        if self.listener_thread is not None:
            self.listener_thread.join()
