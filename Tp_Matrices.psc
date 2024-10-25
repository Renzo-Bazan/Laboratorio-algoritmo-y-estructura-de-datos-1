Algoritmo Tp_Matrices
	Definir Numero_frutas Como Caracter
	Dimension F[2,5]
	fruta = 0
	Para i = 1 Hasta 5 Con Paso 1 Hacer
		Para x = 1 Hasta 1 Con Paso 1 Hacer
			Mostrar "Ingrese un tipo de fruta para la posicion: ","(", x,")","(",i,")"
			Leer F[x,i]
		Fin Para
		Mostrar "Ingrese la cantidad de ese tipo de frutas:"
		Leer Numero_frutas
		F[x,i] = Numero_frutas
	Fin Para
	
	Repetir
		Mostrar "Ingrese la fruta que quiera buscar"
		Leer buscar_fruta
		Para w = 1 Hasta 5 Con Paso 1 Hacer
			Si buscar_fruta = F[1,w] Entonces
				fruta = 1
				cantidad = w
			Fin Si
		Fin Para
		Si fruta = 1 Entonces
			Mostrar ""
			Mostrar "La fruta buscada es: ", buscar_fruta
			Mostrar "y hay: ", cantidad
			Mostrar ""
		SiNo
			Mostrar ""
			Mostrar "La fruta buscada no se encontro, ingrese otra"
			fruta = 0
		Fin Si
	Hasta Que fruta = 1

	Para i = 1 Hasta 5 Con Paso 1 Hacer
		Mostrar "Hay " F[2,i] " " F[1,i]
		Mostrar ""
	Fin Para
	
	
FinAlgoritmo
