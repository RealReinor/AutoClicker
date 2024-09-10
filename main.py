import keyboard
import time
import pyautogui
import json
import threading
import pygetwindow as gw

auto_clicking = False
start_button = ""
quit_button = ""
settings_button = ""

# TO DO LIST
# Complete Settings
# Choose want you want to click
# Menu
# Make EXE file for startup

pyautogui.PAUSE = 0.1


def auto_click():
    global auto_clicking
    while auto_clicking:
        pyautogui.click()
        # keyboard.send("space")
        # keyboard.send("w")


def settings(start_bt, quit_bt, settings_bt):
    global start_button
    global quit_button
    global settings_button

    while True:
        print("\nChoose which button you want to change:")
        print("1: Start Button")
        print("2: Quit Button")
        print("3: Settings Button")
        print("4: Exit")
        while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == "up":
                choice = event.name
                break
        if choice == "1":
            print(f"\nCurrent Start Button: {start_bt}")
            print("Choose what you want to do:")
            print("1: Change Button")
            print("2: Go back")
            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == "up":
                    action = event.name
                    break
            if action == "1":
                print("Please press the new button for Start Button")
                while True:
                    event = keyboard.read_event(suppress=True)
                    if event.event_type == "up":
                        new_key = event.name
                        break
                with open("settings.json", "r+") as f:
                    data = json.load(f)
                    data["start_button"] = new_key
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    start_button = new_key
                print(f"Start Button was changed to {new_key}")
            elif action == "2":
                continue

        elif choice == "2":
            print(f"\nCurrent Quit Button: {quit_bt}")
            print("Choose what you want to do:")
            print("1: Change Button")
            print("2: Go back")

            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == "up":
                    action = event.name
                    break

            if action == "1":
                print("Please press the new button for Quit Button")
                while True:
                    event = keyboard.read_event(suppress=True)
                    if event.event_type == "up":
                        new_key = event.name
                        break
                with open("settings.json", "r+") as f:
                    data = json.load(f)
                    data["quit_button"] = new_key
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    quit_button = new_key
                print(f"Quit Button was changed to {new_key}")
            elif action == "2":
                continue

        elif choice == "3":
            print(f"\nCurrent Settings Button: {settings_bt}")
            print("Choose what you want to do:")
            print("1: Change Button")
            print("2: Go back")

            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == "up":
                    action = event.name
                    break

            if action == "1":
                print("Please press the new button for Settings Button")
                while True:
                    event = keyboard.read_event(suppress=True)
                    if event.event_type == "up":
                        new_key = event.name
                        break
                with open("settings.json", "r+") as f:
                    data = json.load(f)
                    data["settings_button"] = new_key
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    settings_button = new_key
                print(f"Settings Button was changed to {new_key}")
            elif action == "2":
                continue
        elif choice == "4":
            print("\nExiting...")
            print(f"\nStart AutoClicker by pressing \"{start_button.upper()}\" or exit by pressing \""f"{quit_button.upper()}\"")
            print(f"Open settings by pressing \"{settings_button.upper()}\"")
            break


def main():
    with open("info.json") as i, open("settings.json") as s:
        global auto_clicking
        global start_button
        global quit_button
        global settings_button

        info = json.load(i)
        settings_json = json.load(s)

        start_button = settings_json["start_button"]
        quit_button = settings_json["quit_button"]
        settings_button = settings_json["settings_button"]

        print(f"Welcome to \"Anime\" AutoClicker {info["version"]} by {"".join(info["author"])}")
        print(f"\nStart AutoClicker by pressing \"{start_button.upper()}\" or exit by pressing \""f"{quit_button.upper()}\"")
        print(f"Open settings by pressing \"{settings_button.upper()}\"")

        script_window = gw.getActiveWindow()

        while True:
            event = keyboard.read_event()
            if event.name == quit_button and event.event_type == "up":
                if auto_clicking:
                    print("Please stop auto clicking before exiting!")
                else:
                    print("\nEnding AutoClicker")
                    break
            elif event.name == start_button and event.event_type == "up":
                if not auto_clicking:
                    auto_clicking = True
                    t1 = threading.Thread(target=auto_click)
                    t1.start()
                    continue
                else:
                    auto_clicking = False
                    t1.join()
            elif event.name == settings_button and event.event_type == "up":
                if gw.getActiveWindow() == script_window:
                    settings(start_button, quit_button, settings_button)


if __name__ == '__main__':
    main()
