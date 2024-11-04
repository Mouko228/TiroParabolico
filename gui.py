import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

k_padx = 10
k_pady = 5
label_font = ("Helvetica", 10, "bold") 
entry_font = ("Helvetica", 10) 
label_bg = "#f7f7ff"
text_bg = "#f0f0f0"

def setup_gui(root):
    root.title("Calculadora de Tiro Parabolico")
    root.geometry("1050x450")
    root.configure(bg=label_bg)

    inputs = [ 
       ("Projectile Mass (kg):", 1), 
       ("Projectile Diameter (m):", 0.1), 
       ("Gravity (m/s²):", 9.81), 
       ("Spring Constant (N/m):", 1000), 
       ("Target Diameter (m):", 0.5), 
       ("Target Height (m):", 1.5), 
       ("Shooter Height (m):", 1), 
       ("Horizontal Distance (L) (m):", 10), 
       ("Trajectory x-coordinate (m):", 5), 
       ("Trajectory y-coordinate (m):", 3)
    ]

    entries = []

    input_frame = tk.Frame()
    input_frame.configure(bg=label_bg)
    input_frame.grid(row=0, column=0, padx=k_padx, pady=k_pady)

    for i, (entry_label, default_value) in enumerate(inputs):
        # column for labels
        label = tk.Label(input_frame, text=entry_label, bg=label_bg)
        label.grid(row=i, column = 0, padx = k_padx, pady= k_pady)
        
        #column for entries
        entry = tk.Entry(input_frame, bg=entry_bg)
        entry.insert(0, default_value)
        entry.grid(row=i, column=1, padx=k_padx, pady=k_pady)
        
        entries.append(entry)
    
    # Plot --------------------------
    plot_frame = tk.Frame()
    plot_frame.configure(bg=label_bg)
    plot_frame.grid(row=0, column=1, padx=k_padx, pady=k_pady)
    
    fig = Figure(figsize=(5, 4), dpi=100) 
    plot = fig.add_subplot(1, 1, 1)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame) 
    canvas.get_tk_widget().pack(pady=k_pady)
    
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_columnconfigure(1, weight=1)
    # root.grid_columnconfigure(2, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    # root.grid_rowconfigure(0, minsize=100)

    return entries, fig, plot, canvas, [default for _, default in inputs]