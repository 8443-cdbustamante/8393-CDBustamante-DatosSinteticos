#Importación de librerías
import pandas as pd
import random
from faker import Faker

#Declaración y asignación de numeros de registros
num_usuario = 5000

#Instanciación faker
faker = Faker()

#Lista de atributos
atributos = [
    "IdRol",
    "Nombre",
    "Fecha_asigna",
    "Status" 
]

#Arreglo con nombres de roles
nombre =[
    "Operador",
    "Ensamblador",
    "Analista",
    "Programador",
    "Tester",
    "Ayudante"
]

#Arreglo con estados del rol
status = [
    "Activo",
    "Inactivo"
]

#Asignación de atributos a la tabla df
df = pd.DataFrame(columns = atributos)

def idr_gen(n):
    """
    Función que se encarga de crear un id unico con nomenclatura básica
    ...
    
    Return
    ------
    "ROL-"+str(n+1) : str
        id generado con nomenclatura
    """
    return "ROL-"+str(n+1) # id para rol

def nombre_gen():
    """
    Función que toma de forma aleatoria un nombre de rol de su respectiva lista
    ...
    
    Return
    ------
    random.choice(nombre) : str
        nombre de rol seleccionado aleatoriamente
    """
    return random.choice(nombre)

def status_gen():
    """
    Función que toma un estado de forma aleatoria
    ...
    
    Return
    ------
    random.choice(status) : str
        seleccion de estados usando metodo choice de la libreria random
    """
    return random.choice(status)

def fechAsg_gen():
    """
    Función que genera la fecha de asignación del rol
    ...
    
    Return
    ------
    faker.date_between('-2y') : obj datetime.date
        Usa libreria faker para generar fechas entre 2 años antes a la fecha actual
    """
    return faker.date_between('-2y')

#Generacion de datos en cada atributo
df['IdRol'] = [idr_gen(i) for i in range(num_usuario)]
df['Nombre'] = [nombre_gen() for i in range(num_usuario)]
df['Status'] = [status_gen() for i in range(num_usuario)]
df['Fecha_asigna'] = [fechAsg_gen() for i in range(num_usuario)]

#Descarga de datos en archivo .cvs
df.to_csv('Datos_Roles.csv')
