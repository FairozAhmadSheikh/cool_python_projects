import customtkinter as ctk
from tkinter import END
import math

class Calculator:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")  # "light" or "dark"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Beautiful Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Colors
        self.bg_color = "#1a1a1a"
        self.display_color = "#2d2d2d"
        self.number_color = "#404040"
        self.operator_color = "#ff6b35"
        self.equals_color = "#4CAF50"
        self.clear_color = "#f44336"
        
        # Variables
        self.current_expression = ""
        self.total = 0
        
        self.create_widgets()