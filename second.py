import os
import csv

def abc_file_one():
    input_name_materia = input('Escribe el nombre de la materia: ')
    delete_materia_by_name(input_name_materia)

def get_carreras():
    with open('./db/Carreras.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row['NOMBRE,C,40'])

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

def delete_materia_by_name(name_materia):
    original_file = './db/Materias.csv'
    temp_file = './db/temp.csv'

    with open(original_file, 'r', newline='') as file:
        reader = csv.reader(file)
        
        with open(temp_file, 'w', newline='') as temp:
            writer = csv.writer(temp)
            for row in reader:
                if row[1] != name_materia:
                    writer.writerow(row)
    os.replace(temp_file, original_file)

def create_materia(clave, descripción, creditos, fecha_baja, fecha_alta, tipo='L', taller=''):
    pass
