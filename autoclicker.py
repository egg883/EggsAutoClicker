import pyautogui
import time
import threading
import tkinter as tk
import keyboard

class Autoclicker:
    def __init__(self):
        self.delay = "1"
        self.clicking = False
        self.title_text = "Eggs Autoclicker"
        self.made_by_text = "Made by egg883"
        self.keybind = "F4"

        self.bg_color = "#282C34"
        self.fg_color = "#ABB2BF"
        self.button_bg_color = "#3E4451"
        self.button_fg_color = "#FFFFFF"

        self.root = tk.Tk()
        self.root.title(self.title_text)
        self.root.geometry("330x200")
        self.root.iconbitmap("C:/Users/cassi/Desktop/autoclicker/assets/egg.ico")
        self.root.config(bg=self.bg_color)

        self.title_animation_index = 0
        self.title_animation_chars = ["-", "\\", "|", "/"]
        self.animate_title()

        self.delay_label = tk.Label(text="Delay between clicks (in seconds):", bg=self.bg_color, fg=self.fg_color)
        self.delay_label.pack(pady=5)
        self.delay_entry = tk.Entry(bg=self.bg_color, fg=self.fg_color, insertbackground=self.fg_color)
        self.delay_entry.insert(0, str(self.delay))
        self.delay_entry.pack(pady=5)

        self.start_button = tk.Button(text="Start", bg=self.button_bg_color, fg=self.button_fg_color, command=self.start_clicking)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(text="Stop", bg=self.button_bg_color, fg=self.button_fg_color, command=self.stop_clicking, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.keybind = tk.Label(text=f"Press {self.keybind} to begin", bg=self.bg_color, fg=self.fg_color)
        self.keybind.pack(pady=5)

        self.made_by_label = tk.Label(text=self.made_by_text, font=("Helvetica", 8), fg="#bfbfbf", bg="#1f1f1f")
        self.made_by_label.pack(side=tk.BOTTOM, padx=5, pady=5, anchor=tk.SE)

        keyboard.add_hotkey('f4', self.toggle_clicking)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()


    def animate_title(self):
        self.title_animation_index = (self.title_animation_index + 1) % len(self.title_animation_chars)
        animation_char = self.title_animation_chars[self.title_animation_index]
        self.root.title(f"{animation_char} {self.title_text} {animation_char}")
        self.root.after(100, self.animate_title)

    def start_clicking(self):
        self.delay = float(self.delay_entry.get())
        self.clicking = True
        self.title_text = "Eggs Autoclicker - Clicking"
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.click).start()

    def click(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(self.delay)

    def stop_clicking(self, event=None):
        self.clicking = False
        self.title_text = "Eggs Autoclicker - Stopped"
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        time.sleep(1)
        self.title_text = "Eggs Autoclicker"

    def close(self):
        self.clicking = False
        keyboard.remove_hotkey('f4')
        self.root.destroy()

    def toggle_clicking(self):
        if self.clicking:
            self.stop_clicking()
        else:
            self.start_clicking()
Autoclicker()
