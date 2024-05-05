import csv

def study_plans():
    list_planes()

def get_carrera_by_name(clave):
    with open('./db/Carreras.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['CLAVE,C,2'] == clave:
                return row['NOMBRE,C,40']

def list_planes():
    with open('./db/Planes.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            clave = row['CLAVE']
            carrera = row['CARRER']
            carrera_name = get_carrera_by_name(carrera)
            print(clave, carrera, carrera_name)  