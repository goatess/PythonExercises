import sys
import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista en Tcl/Tk")
        main_window.columnconfigure(2, weight=2)
        
        menu = ['Inicio', 'Formación', 'Trayectoria', 'Galería']
        self.menuLabel = ttk.Label(main_window, text='Menu')
        self.listbox = tk.Listbox(main_window, height=4, list=menu, bg='black', fg='white')
        self.listbox.insert(0, *menu)
        self.menuLabel.grid(column=0, row=0, pady=5, padx=5)
        self.listbox.grid(column=0, row=1, pady=5, padx=5)

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
sys.exit(0)