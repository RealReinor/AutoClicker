import keyboard
import pyautogui
import json
import threading
import pygetwindow as gw
import mouse

auto_clicking = False
start_button = ""
quit_button = ""
settings_button = ""
clicking_button = ""

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


def read_key_event():
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == "up":
            return event.name


def update_settings(key, value):
    with open("settings.json", "r+") as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def change_button(current_bt, bt_name):
    print(f"\nCurrent {bt_name}: {current_bt}")
    print("Choose what you want to do:")
    print("1: Change Button")
    print("2: Go back")

    action = read_key_event()

    if action == "1":
        print(f"Please press the new button for {bt_name}")
        new_key = read_key_event()
        update_settings(f"{bt_name.lower().replace(' ', '_')}", new_key)
        print(f"{bt_name} was changed to {new_key}")
        return new_key
    return current_bt


def change_clicking_button(current_bt):
    print(f"\nCurrent Clicking Button: {current_bt}")
    print("Choose what you want to do:")
    print("1: Change Button")
    print("2: Go back")

    action = read_key_event()

    if action == "1":
        print("\nFor clicking button do you use mouse or keyboard")
        print("1: Mouse")
        print("2: Keyboard")

        method = read_key_event()

        if method == "1":
            print("\nPress either the left mouse button or the right mouse button.")
            while True:
                if mouse.is_pressed("left"):
                    new_button = "l_button"
                    break
                elif mouse.is_pressed("right"):
                    new_button = "r_button"
                    break
            update_settings("clicking_button", new_button)
            print(f"Clicking Button was changed to {new_button}")
            return new_button
    return current_bt


def settings(start_bt, quit_bt, settings_bt, clicking_bt):
    global start_button, quit_button, settings_button, clicking_button

    while True:
        print("\nChoose which button you want to change:")
        print("1: Start Button")
        print("2: Quit Button")
        print("3: Settings Button")
        print("4: Change Clicking Button")
        print("5: Exit")

        choice = read_key_event()

        if choice == "1":
            start_button = change_button(start_bt, "Start Button")
        elif choice == "2":
            quit_button = change_button(quit_bt, "Quit Button")
        elif choice == "3":
            settings_button = change_button(settings_bt, "Settings Button")
        elif choice == "4":
            clicking_button = change_clicking_button(clicking_bt)
        elif choice == "5":
            print("\nExiting...")
            print(
                f"\nStart AutoClicker by pressing \"{start_button.upper()}\" or exit by pressing \"{quit_button.upper()}\"")
            print(f"Open settings by pressing \"{settings_button.upper()}\"")
            break


def main():
    with open("info.json") as i, open("settings.json") as s:
        global auto_clicking, start_button,quit_button,settings_button,clicking_button

        info = json.load(i)
        settings_json = json.load(s)

        start_button = settings_json["start_button"]
        quit_button = settings_json["quit_button"]
        settings_button = settings_json["settings_button"]
        clicking_button = settings_json["clicking_button"]

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
                    settings(start_button, quit_button, settings_button,clicking_button)


if __name__ == '__main__':
    main()
