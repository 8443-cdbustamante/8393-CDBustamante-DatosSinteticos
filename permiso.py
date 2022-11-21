#llamado de las librerias autilizar en el script
import pandas as pd
import random
from faker import Faker
import datetime
from datetime import date

#Declaración y asignación del número de entradas
num_usuario = 5000

#Inicialización de la clase Faker
faker = Faker()

# lista de nombres de los atributos corrspondientes a la entidad Permiso
atributos = [
    "IdPermiso",
    "Entidad",
    "Tipo",
    "Fecha_asignar",
    "Fecha_caducar", 
    "Status" 
]

# arreglo con valores para atributo entidad
entidad =[
    "Permisos",
    "Roles",
    "Personal",
    "Departamento",
    "Misil",
    "Componente",
    "Pieza",
    "Proveedor",
    "Parametro"
]

# arreglo con valores para atributo tipo
tipo = [
    "Lectura",
    "Escritura"
]

# arreglo con valores para atributo estado
status = [
    "Vigente",
    "Caducado"
]

# comando para colocar los campos en la tabla
df = pd.DataFrame(columns = atributos)

def idp_gen(n):
    """
    Función para crear la id única
    ...
    Parametro
    n : int
        corresponde al numero indicador del registro correspondiente 
    
    Return
    ------
    "PERM-"+str(n+1) : str
        se crea las identificaciones únicas para los permisos
    """
    return "PERM-"+str(n+1)

def entidad_gen():
    """
    Función para asignar una entidad para el permiso
    ...
    
    Return
    ------
    random.choice(entidad) : str
        generación de la entidad para su asignación en el registro
    """
    return random.choice(entidad)

def tipo_gen():
    """
    Función para asignar el tipo de permiso
    ...
    
    Return
    ------
    random.choice(tipo) : str
        generación del tipo de permiso aleatorio
    """
    return random.choice(tipo)

def fechAsig_gen():
    """
    Función para crear fecha de asignación del permiso
    ...
    
    Return
    ------
    faker.date_between('-10y') : obj datetime.date
        generación de una fecha entre 10 años antes hasta la fecha actual
    """
    return faker.date_between('-10y')

def fechCad_gen(fecha):
    """
    Función para crear fecha de caducidad
    ...
    
    Parametro
    ---------
    fecha : obj Datetime.date
        variable que corresponde a la fecha de asignación del permiso
    
    Return
    ------
    caduca: str
        generación de una fecha con rango de 10 años antes y despues dela fecha actual
    """
    #asignación de objeto con fecha con rango de 10 años antes y despues de fecha actual
    caduca = faker.date_this_decade(True, True)
    #bucle para asegurar que la fecha inicio sea menor a la fecha caduca
    while (caduca <= fecha):
        caduca = faker.date_this_decade(True, True) #genera nueva fecha que cumpla con condicional
    return caduca


def status_gen(fecha):
    """
    Función para la generación de estado del permiso
    ...
    
    Parametros
    ----------
    fecha : obj datetime.date
        fecha correspondiente a la caducidad
    
    Return
    ------
    status[0] :  str
        envía la cadena correspondiente al indice 0 del arreglo status
        
    status[1] : str
        envia la cadena que está en el indice 1 del arreglo status
    """
    #formato de fecha
    frmt = "%Y-%m-%d"
    #Asignación de fecha actual en tipo objeto date
    now = date.today()
    #Fecha actual conseguida
    stime = datetime.datetime.strptime(str(fecha), frmt)
    #Fecha actual
    now1 = datetime.datetime.strptime(str(now), frmt)
    #indicador entero basado en el calculo de edad
    ind = int((stime-now1).days/365.25)
    #asignación de estado de acuerdo al indicador
    if (ind>0):
        return status[0]
    else:
        return status[1]

#Generacion de datos en cada atributo
df['IdPermiso'] = [idp_gen(i) for i in range(num_usuario)]
df['Entidad'] = [entidad_gen() for i in range(num_usuario)]
df['Tipo'] = [tipo_gen() for i in range(num_usuario)]
df['Fecha_asignar'] = [fechAsig_gen() for i in range(num_usuario)]
df['Fecha_caducar'] = [fechCad_gen(i) for i in df["Fecha_asignar"]]
df['Status'] = [status_gen(i) for i in df["Fecha_caducar"]]

#Descarga de datos en archivo .cvs
df.to_csv('Datos_Permisos.csv')
