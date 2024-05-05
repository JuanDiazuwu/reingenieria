import tkinter as tk

from second import abc_file_one
from third import study_plans

def drag_window():
    window = tk.Tk()
    window.title('Opciones')
    window.geometry('600x500')

    button_abc = tk.Button(window, 
                           text="1.- A,B,C de Materias en Planes de Estudio", 
                           command=abc_file_one, 
                           font=("Arial", 20))
    button_study_plans = tk.Button(window, 
                                   text="2.- Listado de Planes de Estudio", 
                                   command=study_plans, 
                                   font=("Arial", 20))
    
    button_abc.pack(fill=tk.BOTH, expand=True)
    button_study_plans.pack(fill=tk.BOTH, expand=True)

    window.mainloop()
