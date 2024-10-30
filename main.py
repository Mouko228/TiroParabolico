# DEPENDENCIES --------------- developer notes
# 1. Tkinter (main, gui) ..... pip install tk
# 2. Matplotlib (gui) ........ pip install matplotlib

import tkinter as tk
from gui import setup_gui

if __name__ == "__main__":
    root = tk.Tk()
    entries, fig, plot, results_label, default_values = setup_gui(root)
    root.mainloop()
