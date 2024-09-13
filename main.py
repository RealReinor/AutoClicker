import customtkinter as ctk
from clicking_manager import ClickingManager


class AutoClickerApp:
    def __init__(self, root_):
        # ClickingManager Instance
        self.clicking_manager = ClickingManager()

        # Variables
        self.click_thread = None
        self.reading_thread = None

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
        start_button = ctk.CTkButton(self.root, text="Start", command=self.start_button_on_click)
        start_button.pack(pady=10)

        # Stop Button
        stop_button = ctk.CTkButton(self.root, text="Stop", command=self.stop_button_on_click)
        stop_button.pack(pady=10)

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


if __name__ == '__main__':
    root = ctk.CTk()
    AutoClickerApp(root)
    root.mainloop()
