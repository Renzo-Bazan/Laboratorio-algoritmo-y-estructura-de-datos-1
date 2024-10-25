Algoritmo TpVectores
	n = 0
	n_mayor = 0
	n_menor = 0
	n_mayor_5 = 0
	suma = 0
	
	Mostrar "¿Cuántos números quiere ingresar?"
	Leer n
	
	Dimension Vec[n]
	
	Para x = 1 Hasta n Con Paso 1 Hacer
		Escribir "Ingrese un número para la posición: ", x
		Leer Vec[x]
	Fin Para
	
	n_mayor = Vec[1]
	n_menor = Vec[1]
	
	Para x = 1 Hasta n - 1 Con Paso 1 Hacer
		Si Vec[x] > n_mayor Entonces
			n_mayor = Vec[x]
		Fin Si
	Fin Para
	
	Para x = 1 Hasta n Con Paso 1 Hacer
		Para x2 <- 1 Hasta n Con Paso 1 Hacer
			Si Vec[x2] < n_menor Entonces
				n_menor = Vec[x2]
			Fin Si
		Fin Para
	Fin Para
	
	Para x = 1 Hasta n Con Paso 1 Hacer
		Si Vec[x] > 5 Entonces
			n_mayor_5 = n_mayor_5 + 1
		Fin Si
	Fin Para
	
	Para x = 1 Hasta n Con Paso 1 Hacer
		suma = suma + Vec[x]
	Fin Para
	
	Mostrar "De los números ingresados el mayor es: ", n_mayor
	Mostrar ""
	Mostrar "De los números ingresados el menor es: ", n_menor
	Mostrar ""
	Mostrar "La cantidad de números mayores a 5 son: ", n_mayor_5
	Mostrar ""
	Mostrar "La suma de todos los números ingresados es: ", suma
FinAlgoritmo

