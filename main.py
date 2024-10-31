# DEPENDENCIES --------------- developer notes
# 1. Tkinter (main, gui) ..... pip install tk
# 2. Matplotlib (gui) ........ pip install matplotlib
# 3. Numpy (backend, gui) .... pip install numpy

import tkinter as tk
from gui import setup_gui
from gui import k_padx, k_pady, label_bg, label_font, entry_bg, entry_font

def calculate():
    return 0

def reset_inputs():
    for entry, default in zip(entries,default_values):
        entry.delete(0, tk.END)
        entry.insert(0, default)

if __name__ == "__main__":
    root = tk.Tk()

    entries, fig, plot, default_values = setup_gui(root)
    
    result_frame = tk.Frame()
    result_frame.configure(bg=label_bg)
    result_frame.grid(row=0, column=2, padx=k_padx, pady=k_pady)    

    calculate_button = tk.Button(result_frame, text="Calculate...", command=lambda: calculate())
    calculate_button.pack()

    reset_button = tk.Button(result_frame, text="Reset values", command=lambda: reset_inputs())
    reset_button.pack()
    
    results_label = tk.Label(result_frame, text="Results: ...make a calculation",bg=label_bg)
    results_label.pack(pady=k_pady)

    root.mainloop()
