#Importación de librerias
import pandas as pd
import random
from faker import Faker

#Declaración y asignación del numero de registros solicitados
num_usuario = 5000

#Instanciación del proceso faker
faker = Faker()

#Lista de atributos de misil
atributos = [
    "IdMisil",
    "Nombre",
    "Tipo",
    "Fecha_fabrica",
    "Status"  
]

#Lista de nombres para misiles
nombre =[
    "misil-A",
    "misil-B",
    "misil-C",
    "misil-D",
    "misil-E",
    "misil-F"
]

#Lista de tipos de misiles
tipo = [
    "Cinetico",
    "Explosivo",
    "Nuclear"
]

#Lista de estados del misil en cuestión
status = [
    "Listo",
    "En proceso",
    "Incompleto"
]

#asignacion de atributos a la tabla definida
df = pd.DataFrame(columns = atributos)

def idm_gen(n):
    """
    Función que se encarga de crear un id unico con nomenclatura básica
    ...
    
    Parametros
    ----------
    n : int
        representa el numero de indice correspondiente al registro
    
    Return
    ------
    "MSL--"+str(n+1) : str
        nomenclatura única de identificación del misil correspondiente
    """
    return "MSL-"+str(n+1)

def nombre_gen():
    """
    Función para asignación del nombre del misil
    ...
    
    Return
    ------
    "random.choice(nombre) : str
        De forma aleatoria, se asigna un nombre al misil
    """
    return random.choice(nombre)

def tipo_gen():
    """
    Función que dá el tipo de misil
    ...
    
    Return
    ------
    random.choice(tipo): str
        Selección aleatoria de tipo de misil
    """
    return random.choice(tipo)

def fechFab_gen():
    """
    Función para crear fecha de fabricacion
    ...
    
    Return
    ------
    faker.date_between('-5y'): obj datetime.date
        generación de una fecha entre 5 años antes, hastala fecha actual
    """
    return faker.date_between('-5y')

def status_gen():
    """
    Función para asignar el estado del misil
    ...
    
    Return
    ------
    random.choice(status) : str
        selección del estado del misil
    """
    return random.choice(status)

#Generacion de datos en cada atributo
df['IdMisil'] = [idm_gen(i) for i in range(num_usuario)]
df['Nombre'] = [nombre_gen() for i in range(num_usuario)]
df['Tipo'] = [tipo_gen() for i in range(num_usuario)]
df['Fecha_fabrica'] = [fechFab_gen() for i in range(num_usuario)]
df['Status'] = [status_gen() for i in range(num_usuario)]

#Descarga de datos en archivo .cvs
df.to_csv('Datos_Misil.csv')
