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

ruta = Path("Curso Python") / "Día 6" / "practicas_path.py"


# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario


ruta = Path.home() / "Curso Python" / "Día 6" / "practicas_path.py"
print(ruta)


# from os import system

# nombre = input("Dime tu numbre : ")

# edad = input("Dime tu edad : ")

# system('cls')

# print(nombre)
# print(edad)


# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

def abrir_leer(archivo_abrir):
    archivo = open(archivo_abrir,"r")
    contenido = archivo.read()
    archivo.close()
    return contenido


# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo_sobrescribir):
    archivo = open(archivo_sobrescribir, "w")
    archivo.write("contenido eliminado")
    archivo.close()


# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y 
# lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".

def registro_error(archivo1):
    archivo = open(archivo1,"a")
    archivo.write("\nSe ha registrado un error de ejecución\n")
    archivo.close()