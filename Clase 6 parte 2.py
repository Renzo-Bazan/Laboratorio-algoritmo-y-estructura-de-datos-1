# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

# Recuerda importar Path del módulo pathlib, y utilizar el método home()

from pathlib import Path
ruta_base = Path.home()

# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path

from pathlib import Path

ruta = Path(C:) / "Curso Python" / "Día 6" / "practicas_path.py"


# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario





# from os import system

# nombre = input("Dime tu numbre : ")

# edad = input("Dime tu edad : ")

# system('cls')

# print(nombre)
# print(edad)


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

def abrir_leer(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no se encuentra en la ruta especificada."
    except Exception as e:
        return f"Ocurrió un error: {e}"


# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"


# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".