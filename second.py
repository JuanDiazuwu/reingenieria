import os
import csv
import re
import tkinter as tk
from tkinter import ttk, messagebox

def create_materia_tab(notebook):
    # Pestaña para crear una materia
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Crear Materia")

    tk.Label(tab, text="Clave: ").grid(row=0, column=0)
    clave_entry = tk.Entry(tab)
    clave_entry.grid(row=0, column=1)

    tk.Label(tab, text="Descripción: ").grid(row=1, column=0)
    descripcion_entry = tk.Entry(tab)
    descripcion_entry.grid(row=1, column=1)

    tk.Label(tab, text="Nº Sesiones: ").grid(row=2, column=0)
    nsesion_entry = tk.Entry(tab)
    nsesion_entry.grid(row=2, column=1)

    tk.Label(tab, text="Duración: ").grid(row=3, column=0)
    duracion_entry = tk.Entry(tab)
    duracion_entry.grid(row=3, column=1)

    tk.Label(tab, text="Taller (S/N): ").grid(row=4, column=0)
    taller_entry = tk.Entry(tab)
    taller_entry.grid(row=4, column=1)

    tk.Label(tab, text="Fecha Alta (DD/MM/AAAA): ").grid(row=5, column=0)
    fecalt_entry = tk.Entry(tab)
    fecalt_entry.grid(row=5, column=1)

    tk.Label(tab, text="Fecha Baja (DD/MM/AAAA): ").grid(row=6, column=0)
    fecbaj_entry = tk.Entry(tab)
    fecbaj_entry.grid(row=6, column=1)

    tk.Label(tab, text="Tipo (L): ").grid(row=7, column=0)
    tipo_entry = tk.Entry(tab)
    tipo_entry.grid(row=7, column=1)

    def create_materia():
        # Obtener los valores
        clave = clave_entry.get()
        descripcion = descripcion_entry.get()
        nsesion = nsesion_entry.get()
        duracion = duracion_entry.get()
        taller = taller_entry.get()
        fecalt = fecalt_entry.get()
        fecbaj = fecbaj_entry.get()
        tipo = tipo_entry.get()

        # Escribir los datos en la BD
        with open('./db/Materias.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([clave, descripcion, nsesion, duracion, taller, fecalt, fecbaj, tipo])

    create_button = tk.Button(tab, text="Crear", command=create_materia)
    create_button.grid(row=8, column=0, columnspan=2)

def delete_materia_tab(notebook):
    # Pestaña para eliminar una materia
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Eliminar Materia")

    tk.Label(tab, text="Clave de la materia a eliminar: ").grid(row=0, column=0)
    clave_entry = tk.Entry(tab)
    clave_entry.grid(row=0, column=1)
    def delete_materia():
        # Función para eliminar una materia
        clave = clave_entry.get()
        original_file = './db/Materias.csv'
        temp_file = './db/temp.csv'

        with open(original_file, 'r', newline='') as file:
            reader = csv.reader(file)

            with open(temp_file, 'w', newline='') as temp:
                writer = csv.writer(temp)
                for row in reader:
                    if row[0] != clave:
                        writer.writerow(row)
        os.replace(temp_file, original_file)    
    delete_button = tk.Button(tab, text="Eliminar", command=delete_materia)
    delete_button.grid(row=1, column=0, columnspan=2)

def update_materia_tab(notebook):
    # Pestaña para actualizar una materia
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Actualizar Materia")

    tk.Label(tab, text="Clave de la materia a actualizar: ").grid(row=0, column=0)
    clave_entry = tk.Entry(tab)
    clave_entry.grid(row=0, column=1)

    def buscar_materia():
        # Función para buscar los datos de la materia y llenar los campos de entrada
        clave = clave_entry.get()

        # Abrir el archivo Materias.csv y buscar la materia por clave
        with open('./db/Materias.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == clave:
                    # Rellenar los campos de entrada con la información encontrada
                    desc_entry.delete(0, tk.END)  # Limpiar el campo antes de rellenarlo
                    desc_entry.insert(0, row[1])
                    sesion_entry.delete(0, tk.END)
                    sesion_entry.insert(0, row[2])
                    duracion_entry.delete(0, tk.END)
                    duracion_entry.insert(0, row[3])
                    taller_entry.delete(0, tk.END)
                    taller_entry.insert(0, row[4])
                    fecalt_entry.delete(0, tk.END)
                    fecalt_entry.insert(0, row[5])
                    fecbaj_entry.delete(0, tk.END)
                    fecbaj_entry.insert(0, row[6])
                    tipo_entry.delete(0, tk.END)
                    tipo_entry.insert(0, row[7])
                    break  # Terminar el bucle una vez que se encuentre la materia

    buscar_button = tk.Button(tab, text="Buscar", command=buscar_materia)
    buscar_button.grid(row=0, column=2)

    tk.Label(tab, text="Nueva descripción: ").grid(row=1, column=0)
    desc_entry = tk.Entry(tab)
    desc_entry.grid(row=1, column=1)

    tk.Label(tab, text="Nuevo nº sesiones: ").grid(row=2, column=0)
    sesion_entry = tk.Entry(tab)
    sesion_entry.grid(row=2, column=1)

    tk.Label(tab, text="Nueva duración: ").grid(row=3, column=0)
    duracion_entry = tk.Entry(tab)
    duracion_entry.grid(row=3, column=1)

    tk.Label(tab, text="Nuevo taller (S/N): ").grid(row=4, column=0)
    taller_entry = tk.Entry(tab)
    taller_entry.grid(row=4, column=1)

    tk.Label(tab, text="Nueva fecha alta (DD/MM/AAAA): ").grid(row=5, column=0)
    fecalt_entry = tk.Entry(tab)
    fecalt_entry.grid(row=5, column=1)

    tk.Label(tab, text="Nueva fecha baja (DD/MM/AAAA): ").grid(row=6, column=0)
    fecbaj_entry = tk.Entry(tab)
    fecbaj_entry.grid(row=6, column=1)

    tk.Label(tab, text="Nuevo tipo (L): ").grid(row=7, column=0)
    tipo_entry = tk.Entry(tab)
    tipo_entry.grid(row=7, column=1)

    def update_materia():
        # Función para actualizar una materia
        original_file = './db/Materias.csv'
        temp_file = './db/temp.csv'
        clave = clave_entry.get()

        # Pedir al usuario los nuevos valores
        descripcion = desc_entry.get()
        nsesion = sesion_entry.get()
        duracion = duracion_entry.get()
        taller = taller_entry.get()
        fecalt = fecalt_entry.get()
        fecbaj = fecbaj_entry.get()
        tipo = tipo_entry.get()

        # Abrir el archivo original y el temporal
        with open(original_file, 'r', newline='') as file:
            reader = csv.reader(file)
            with open(temp_file, 'w', newline='') as temp:
                writer = csv.writer(temp)
                for row in reader:
                    if row[0] == clave:
                        # Actualizar los campos
                        row[1] = descripcion
                        row[2] = nsesion
                        row[3] = duracion
                        row[4] = taller
                        row[5] = fecalt
                        row[6] = fecbaj
                        row[7] = tipo
                    writer.writerow(row)
        # Reemplazar el archivo original con el temporal
        os.replace(temp_file, original_file)

    update_button = tk.Button(tab, text="Actualizar", command=update_materia)
    update_button.grid(row=8, column=0, columnspan=2)

def search_materia_tab(notebook):
    # Pestaña para buscar una materia
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Buscar Materia")

    def search_materia():
        clave = clave_entry.get()  # Obtener la clave de la materia desde la interfaz
        with open('./db/Materias.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['CLAVE,C,3'] == clave:
                    # Mostrar la información en un mensaje
                    message = f"Descripción: {row['DESCRI,C,35']}\n" \
                              f"Número de sesiones: {row['NSESIO,C,3']}\n" \
                              f"Duración: {row['DURSES,C,3']}\n" \
                              f"Taller: {row['TALLER,C,3']}\n" \
                              f"Fecha de alta: {row['FECALT,D']}\n" \
                              f"Fecha de baja: {row['FECBAJ,C,10']}\n" \
                              f"Tipo: {row['TIPO,C,1']}"
                    tk.messagebox.showinfo("Información de la materia", message)

    tk.Label(tab, text="Clave de la materia a buscar: ").grid(row=0, column=0)
    clave_entry = tk.Entry(tab)
    clave_entry.grid(row=0, column=1)

    search_button = tk.Button(tab, text="Buscar", command=search_materia)
    search_button.grid(row=1, column=0, columnspan=2)

def abc_file_one():
    # Función para abrir una ventana con pestañas de CRUD para las materias
    ventana = tk.Toplevel()
    ventana.title("CRUD de Materias")

    notebook = ttk.Notebook(ventana)

    create_materia_tab(notebook)
    delete_materia_tab(notebook)
    update_materia_tab(notebook)
    search_materia_tab(notebook)

    notebook.pack(expand=True, fill="both")

def delete_carrera_by_name(name_carrera):
    original_file = './db/Carreras.csv'
    temp_file = './db/temp.csv'

    with open(original_file, 'r', newline='') as file:
        reader = csv.reader(file)
        
        with open(temp_file, 'w', newline='') as temp:
            writer = csv.writer(temp)
            for row in reader:
                if row[1] != name_carrera:
                    writer.writerow(row)
    os.replace(temp_file, original_file)

def get_materias():
    with open('./db/Materias.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row['DESCRI,C,35'])

