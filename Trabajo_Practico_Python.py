def validacion_nombre(nombre_ingresado):
    if nombre_ingresdo.replace(" ", "").isalpha():
        if nombre_ingresdo.upper()!= "REPETIR":
            return True
    return False

def vocales_consonantes(nombres):
    n_vocales = 0
    n_consonantes = 0
    vocales = "aeiouáéíóú"
    for nombre in nombres:
        nombre = nombre.lower()
        for letra in nombre:
            if letra.isalpha():
                if letra in vocales:
                    n_vocales = n_vocales+1
                else:
                    n_consonantes = n_consonantes + 1
    return f"Hay {n_consonantes} consonantes y hay {n_vocales} vocales"

def contador_nombres(nombres):
    for nombre in nombres:
        cant_palabras = len(nombre.split())
        print(f"El nombre {nombre}, tiene {cant_palabras} palabra/s")

def bucar_inicial(nombres, inicial):
    nomb_inicial = []
    for nombre in nombres:
        if nombre.lower().startswith(inicial.lower()):
            nomb_inicial.append(nombre)
    if not nomb_inicial:
        return f"no hay nombres que inicien con la letra {inicial}"
    else:
        return f"Los nombres que comienzan con {inicial} son {', '.join(nomb_inicial)}"

def verificar_nombre(nombres, nombre_buscado):
    for nombre in nombres:
        if nombre == nombre_buscado:
            return "El nombre ingresado si se encuentra en la lista"
    
    return "El  nombre ingresado no se encuentra en la lista"

def nomb_5(nombres):
    cant_nomb_5 = []
    contador = 0
    for nombre in nombres:
        if len(nombre.replace(" ","")) > 5:
            contador = contador + 1
            cant_nomb_5.append(nombre)
    return contador

def mayus_minus(nombres, min_may):
    nomb_minus = []
    nomb_mayus = []
    for nombre in nombres:
        nomb_minus.append(nombre.lower())
        nomb_mayus.append(nombre.upper())
    if min_may == "mayusculas":
        return nomb_mayus
    if min_may == "minusculas":
        return nomb_minus

def nomb_minus5(nombres):
    cant_nomb_minus5 = []
    contador2 = 0
    for nombre in nombres:
        if len(nombre.replace(" ","")) < 5:
            contador2 = contador2 + 1
            cant_nomb_minus5.append(nombre)
    return contador2



nombres = []
while True:
    nombre_ingresdo = input("""Ingrese el nombre del estudiante.
 Para ver los nombres guardados, ingrese: repetir
 Para terminar, ingrese: fin 
 Ingrese nombre: """)
    
    if nombre_ingresdo.upper() == "FIN":                
        break

    if nombre_ingresdo.upper() == "REPETIR":        
        print("los nombres ingresados son: ", ", ".join(nombres))

    if validacion_nombre(nombre_ingresdo):
        nombres.append(nombre_ingresdo)
    else:
        print("INGRESE UN NOMBRE VALIDO.")



print("Menu de opciones:")
print("1)  Mostar los nombres ingresados.")
print("2)  Mostrar los nombres en orden alfabetico.")
print("3)  Mostrar el nombre mas largo y el mas corto.")
print("4)  Mostrar cuántas vocales y consonantes hay en total en todos los nombres combinados.")
print("5)  Mostrar cuántas palabras hay en cada nombre")
print("6)  Mostrar los nombres invertidos.")
print("7)  Mostrar todos los nombres que comiencen con una letra especifica.")
print("8)  Verificar si un nombre se encuentra en la lista.")
print("9)  Contar cuántos nombres tienen más de 5 caracteres")
print("10) Convertir todos los nombres a mayúsculas o minúsculas")
print("11) Contar cuántos nombres tienen menos de 5 caracteres")
print("")
print("0)  Para terminar")
print("")
print("")
while True:
    opcion = int(input("Ingrese el numero de la opcion que desea utilizar: "))

    if opcion == 1:
        print("los nombres ingresados son: ", nombres)
        print("")

    if opcion == 2:
        nombres_alf = sorted(nombres)  
        print(f"Los nombres ingresados ordenados alfabeticamente: , {','.join(nombres_alf)}")
        print("")

    if opcion == 3:
        nombre_largo = max(nombres, key=len)
        nombre_corto = min(nombres, key=len)
        print("El nombre mas largo es: ", nombre_largo)
        print("El nombre mas corto es: ", nombre_corto)
        print("")

    if opcion == 4:
        print(vocales_consonantes(nombres))
        print("")

    if opcion == 5:
        print(contador_nombres(nombres))
        print("")

    if opcion == 6:
        nombres_espejo = [nombre[::-1] for nombre in nombres]
        print(f"Los nombres invertidos son: {', '.join(nombres_espejo)}")
        print("")

    if opcion == 7:
        inicial = input("ingrese la inicial con con la que quiere buscar los nombres: ")
        print(bucar_inicial(nombres, inicial))
        print("")

    if opcion == 8:
        nombre_buscado = input("Ingresa un nombre para verificar si se encuentra en la lista")
        print(verificar_nombre(nombres, nombre_buscado))
        print("")

    if opcion == 9:
        valor = nomb_5(nombres)
        print(f"Hay {valor} nombre/s con mas de 5 caracteres.")
        print("")

    if opcion == 10:
        min_may = input("Quiere transformar los nombres a mayusculas o minusculas?")
        print(mayus_minus(nombres, min_may))
    
    if opcion == 11:
        valor2 = nomb_minus5(nombres)
        print(f"Hay {valor2} nombre/s con menos de 5 caracteres.")
        print("")

    if opcion == 0:
        break