"""A menu for loading routines and command books."""

import tkinter as tk
from src.gui.menu.file import File

class Menu(tk.Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.file = File(self, tearoff=0)
