# main app
from typing import Optional, Tuple, Union
import customtkinter as ctk
from frames.login_frame import LoginFrame

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("ECORYS - 224")
        self.resizable(0, 0)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_width = int(self.screen_width * 0.84)
        self.window_height = int(self.screen_height * 0.84)
        self.x_position = (self.screen_width - self.window_width) // 2
        self.y_position = (self.screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{self.x_position}+{self.y_position}")

        # Create login frame
        login_frame_instance = LoginFrame(self)

if __name__ == "__main__" :
    app = App()
    app.mainloop()