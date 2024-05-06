import tkinter as tk
from tkinter import ttk
import csv
import os

# Función para obtener el nombre de la materia dado su clave
def get_materia_name(clave):
    with open(os.path.join('db', 'Materias.csv'), newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila que contiene los encabezados
        for row in reader:
            if row:  # Verificar si la fila no está vacía
                if row[0] == clave:  # Acceder al primer elemento de la fila como la clave
                    return row[1]  # Devolver el segundo elemento de la fila como el nombre de la materia
    return "N/A"


# Función para mostrar los planes de estudio
def show_study_plans():
    # Crear una ventana
    window = tk.Tk()
    window.title('Planes de Estudio')
    window.geometry('800x600')

    # Crear un Treeview para mostrar los datos en forma de tabla
    tree = ttk.Treeview(window, columns=("CLAVE", "CARRER", "MATERI", "FECALT", "FECBAJ", "AREA", "REQSIM", "REQUI1", "REQUI2", "REQUI3", "REQUI4", "SEMEST"))
    tree.heading("#0", text="No.")
    tree.heading("CLAVE", text="CLAVE")
    tree.heading("CARRER", text="CARRERA")
    tree.heading("MATERI", text="MATERIA")
    tree.heading("FECALT", text="FECHA ALTA")
    tree.heading("FECBAJ", text="FECHA BAJA")
    tree.heading("AREA", text="AREA")
    tree.heading("REQSIM", text="REQUISITO")
    tree.heading("REQUI1", text="REQUISITO #1")
    tree.heading("REQUI2", text="REQUISITO #2")
    tree.heading("REQUI3", text="REQUISITO #3")
    tree.heading("REQUI4", text="REQUISITO #4")
    tree.heading("SEMEST", text="SEMESTRE")

    # Leer los datos del archivo CSV y añadirlos a la tabla
    with open(os.path.join('db', 'Planes.csv'), newline='') as file:
        reader = csv.DictReader(file)
        column_widths = {}  # Diccionario para almacenar el ancho máximo de cada columna
        for idx, row in enumerate(reader, 1):
            # Obtener el nombre de la materia
            materia_name = get_materia_name(row["MATERI"])
            reqsim_name = get_materia_name(row["REQSIM"])
            requi1_name = get_materia_name(row["REQUI1"])
            requi2_name = get_materia_name(row["REQUI2"])
            requi3_name = get_materia_name(row["REQUI3"])
            requi4_name = get_materia_name(row["REQUI4"])
            # Insertar fila en el Treeview
            tree.insert("", "end", text=idx, values=(row["CLAVE"], row["CARRER"], materia_name, row["FECALT"], row["FECBAJ"], row["AREA"], reqsim_name, requi1_name, requi2_name, requi3_name, requi4_name, row["SEMEST"]))
            # Actualizar el ancho máximo de cada columna
            for key, value in row.items():
                column_widths.setdefault(key, 0)
                column_widths[key] = max(column_widths[key], len(str(value)))

    # Establecer el ancho de cada columna en función del ancho máximo
    for column_id, width in column_widths.items():
        tree.column(column_id, width=width * 10)  # Multiplicar por 10 para ajustar el ancho

    # Añadir el Treeview a la ventana
    tree.pack(expand=True, fill=tk.BOTH)

    # Ajustar automáticamente el tamaño de la ventana al contenido
    window.update()
    window.geometry(f"{tree.winfo_width()}x{tree.winfo_height()}")

    # Ejecutar el loop de la ventana
    window.mainloop()

