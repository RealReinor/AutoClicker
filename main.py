import customtkinter as ctk
from clicking_manager import ClickingManager
from settings_manager import SettingsManager


class AutoClickerApp:
    def __init__(self, root_):
        # ClickingManager Instance
        self.clicking_manager = ClickingManager()
        self.settings_manager = SettingsManager()

        # Variables
        self.click_thread = None
        self.reading_thread = None
        self.start_button = None
        self.stop_button = None
        self.record_button = None

        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # App settings
        self.root = root_
        self.root.geometry("320x480")
        self.root.title("AutoClicker")

        # UI elements
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    def create_widgets(self):
        # Title
        title = ctk.CTkLabel(self.root, text='Welcome To AutoClicker By "Reinor"', text_color="white", font=("Helvetica", 14, "bold"))
        title.pack(padx=10, pady=10)

        # Start Button
        self.start_button = ctk.CTkButton(self.root, text=f"Start ({self.settings_manager.start_button.upper()})", command=self.start_button_on_click)
        self.start_button.pack(pady=10)

        # Stop Button
        self.stop_button = ctk.CTkButton(self.root, text="Stop", command=self.stop_button_on_click)
        self.stop_button.pack(pady=10)

        # Record Button
        self.record_button = ctk.CTkButton(self.root, text='Record', command=self.on_record)
        self.record_button.pack(pady=50)

        # Start Reading Keys
        self.clicking_manager.read_key_event()

    def start_button_on_click(self):
        if not self.clicking_manager.auto_clicking:
            self.clicking_manager.start_auto_click()

    def stop_button_on_click(self):
        if self.clicking_manager.auto_clicking:
            self.clicking_manager.stop_auto_click()


    def on_close(self):
        self.clicking_manager.stop_auto_click()
        self.clicking_manager.stop_key_listener()
        root.destroy()

    def on_record(self):
        if not self.clicking_manager.auto_clicking:
            self.settings_manager.record_new_start_button_key()
            self.start_button.configure(text=f"Start ({self.settings_manager.start_button.upper()})")


if __name__ == '__main__':
    root = ctk.CTk()
    AutoClickerApp(root)
    root.mainloop()
