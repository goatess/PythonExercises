import sys
import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, window):
        super().__init__(window)

        window.columnconfigure(5, weight=5)
        self.seleccionado = tk.StringVar()
        self.yes = ttk.Radiobutton(window, text='Sí', value='1', variable=self.seleccionado)
        self.no = ttk.Radiobutton(window, text = 'No', value='2', variable=self.seleccionado)
        self.perhaps = ttk.Radiobutton(window, text = 'Quizás', value='3', variable=self.seleccionado)
        self.restart = ttk.Button(window, text='Restart', command=self.restart)
        self.quitB = ttk.Button(window, text = 'Quit', command = self.quitApp)
        self.formLabel = ttk.Label(window, text='Formulario')

        self.formLabel.grid(column=0, row=0, pady=5, padx=5)
        self.yes.grid(column=0, row=1, pady=5, padx=5)
        self.no.grid(column=0, row=2, pady=5, padx=5)
        self.perhaps.grid(column=0, row=3,pady=5, padx=5)
        self.restart.grid(column=0, row=4, pady=5, padx=5)
        self.quitB.grid(column=0, row=5, pady=5, padx=5)

    def restart(self):
        self.seleccionado.set('0')

    def quitApp(self):
        window.quit()   
        
window = tk.Tk()
app = Application(window)
app.mainloop()
sys.exit(0)