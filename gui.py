import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def setup_gui(root):
    root.title("Calculadora de Tiro Parabolico")
    root.geometry("800x600")

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

    for entry_label, default_value in inputs:
        label = tk.Label(root, text=entry_label)
        label.pack()
        entry = tk.Entry(root)
        entry.insert(0, default_value)
        entry.pack()
        entries.append(entry)
    
    #fig = Figure(figsize=(5, 4), dpi=100) 
    #plot = fig.add_subplot(1, 1, 0)
    fig, plot = 0, 0

    #canvas = FigureCanvasTkAgg(fig, master=root) 
    #canvas.get_tk_widget().pack()

    results_label = tk.Label(root, text="Results: ...make a calculation")
    results_label.pack()

    return entries, fig, plot, results_label, [default for _, default in inputs]