from tkinter.ttk import *
from tkinter import *
import re

import gui_display_animations

class App:

    def __init__(self):
        root = Tk()
        gui_display_animations.Main(root)
        root.mainloop()

if __name__ == "__main__":
    sys.exit(App())
 
 
