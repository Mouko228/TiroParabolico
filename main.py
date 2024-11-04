# DEPENDENCIES --------------- developer notes
# 1. Tkinter (main, gui) ..... pip install tk
# 2. Matplotlib (gui) ........ pip install matplotlib
# 3. Numpy (backend, gui) .... pip install numpy

import tkinter as tk
import numpy as np
from gui import setup_gui
from gui import k_padx, k_pady, label_bg, label_font, entry_bg, entry_font
from backend import parabola, convert

def calculate():
    try:
        values = []
        for entry in entries:
            values.append(float(entry.get()))
        entry_mass, entry_diameter, entry_g, entry_k_spring, entry_target_d, entry_target_h, entry_shooter_height, entry_hd, entry_x2, entry_y2 = values
        x1,y1,x2,y2,x3,y3,mass,k,g = convert(entry_mass, entry_diameter, entry_g, entry_k_spring, entry_target_d, entry_target_h, entry_shooter_height, entry_hd, entry_x2, entry_y2)
        theta, r, a, b, c= parabola(x1,y1,x2,y2,x3,y3,mass,k,g)
        results_label.config(text = f"Results: \nyou must aim {theta}° Degrees, \nwith a compression of {r} units")
        plot.clear()
        x=np.linspace(0, x3+entry_diameter,100)
        y=a*x**2 +b*x+c
        plot.plot(x,y, label=f'$y = {a}x^2 + {b}x + {c}$')
        plot.set_xlabel('x')
        plot.set_ylabel('y')
        plot.grid(True)
        plot.axhline(0, color='black', linewidth=0.5)
        plot.axvline(0, color='black', linewidth=0.5)
        plot.legend()
        canvas.draw()
    except:
        plot.clear()
        canvas.draw()
        results_label.config(text = f"The values you entered can't\nbe traced into a\ntrajectory")

    
def reset_inputs():
    for entry, default in zip(entries,default_values):
        entry.delete(0, tk.END)
        entry.insert(0, default)

if __name__ == "__main__":
    root = tk.Tk()

    entries, fig, plot, canvas, default_values = setup_gui(root)
    
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
