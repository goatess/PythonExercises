import sys
import tkinter
from tkinter import ttk

def restart():
    seleccionado.set('0')

def quitApp():
    window.quit()
    
window = tkinter.Tk()
window.columnconfigure(5, weight=5)
seleccionado = tkinter.StringVar()

yes = ttk.Radiobutton(window, text='Sí', value='1', variable=seleccionado)
no = ttk.Radiobutton(window, text = 'No', value='2', variable=seleccionado)
perhaps = ttk.Radiobutton(window, text = 'Quizás', value='3', variable=seleccionado)

restart = ttk.Button(window, text='Restart', command=restart)
quitB = ttk.Button(window, text = 'Quit', command = quitApp)

def locateButtons():
    yes.grid(column=0, row=1, pady=5, padx=5)
    no.grid(column=0, row=2, pady=5, padx=5)
    perhaps.grid(column=0, row=3,pady=5, padx=5)
    restart.grid(column=0, row=4, pady=5, padx=5)
    quitB.grid(column=0, row=5, pady=5, padx=5)

locateButtons()
window.mainloop()	
sys.exit(0)
