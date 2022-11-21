import pandas as pd
import random
from faker import Faker

num_usuario = 5000
faker = Faker()

atributos = [
    "IdPieza",
    "Nombre",
    "Tipo",
    "Cantidad",
    "Fecha_fabrica"  
]

nombre =[
    "combustible-A",
    "combustible-B",
    "combustible-C",
    "tornillo-A",
    "tornillo-B",
    "Plancha acero",
    "Plancha aluminio",
    "Plancha kevlar",
    "Tarjeta PCB",
    "Procesadores",
    "Panel solar",
    "Sensor-A",
    "Sensor-B",
    "Sensor-C",
    "Antena-A",
    "Antena-B"
    "OS-A",
    "OS-B",
    "system-A",
    "system-B"
]

tipo = [
    "Quimico",
    "Mecanico",
    "Electronico",
    "Software"
]

df = pd.DataFrame(columns = atributos)

#funciones para generar los atributos aleatoriamente
def id_gen(n):
    """
    Función para crear la id única
    ...
    Parametro
    n : int
        corresponde al numero indicador del registro correspondiente 
    
    Return
    ------
    "PZ-"+str(n+1) : str
        se crea las identificaciones únicas para los permisos
    """
    return "PZ-"+str(n+1)

def nombre_gen():
    """
    Función para asignación del nombre de la pieza
    ...
    
    Return
    ------
    "random.choice(nombre) : str
        De forma aleatoria, se asigna un nombre a la pieza
    """
    return random.choice(nombre)

def tipo_gen(name):
    """
    Función que dá el tipo de misil
    ...
    
    Return
    ------
    random.choice(tipo): str
        Selección aleatoria de tipo de misil
    """
    #obtencion del indice de nombre
    ind = nombre.index(name)
    if (ind >= 0 and ind <=2):
        return tipo[0]
    elif (ind >= 3 and ind <=7):
        return tipo[1]
    elif (ind >= 8 and ind <=15):
        return tipo[2]
    elif (ind >= 16 and ind <=19):
        return tipo[3]
    return "NA"

def cantidad_gen():
    """
    Función para crear la cantidad
    ...
   
    Return
    ------
   random.randint(1,100)) : int
        se crea un entero entre 1 a 100
    """
    return random.randint(1,100)

def fechFab_gen():
    """
    Función para crear fecha de fabricación
    ...
    
    Return
    ------
    faker.date_between('-10y') : obj datetime.date
        generación de una fecha entre 10 años antes hasta la fecha actual
    """
    return faker.date_between('-10y')

#Generacion de datos en cada atributo
df['IdPieza'] = [id_gen(i) for i in range(num_usuario)]
df['Nombre'] = [nombre_gen() for i in range(num_usuario)]
df['Tipo'] = [tipo_gen(i) for i in df['Nombre']]
df['Cantidad'] = [cantidad_gen() for i in range(num_usuario)]
df['Fecha_fabrica'] = [fechFab_gen() for i in range(num_usuario)]

#Descarga de datos en archivo .cvs
df.to_csv('Datos_Pieza.csv')
