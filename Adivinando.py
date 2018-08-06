import random 

jugar = 1
codigoGenerado = ''
codigoIngresado = ''

while jugar == 1:
	print("Bienvenido/a a Adivinando")
	print("Elija la dificultad del juego \n1. Fácil \n2. Media \n3. Difícil")
	dificultad = int(input("Ingrese el número de dificultad: "))

	if dificultad == 1:
	 	cantidadDigitos = 3
	elif dificultad == 2:
	 	cantidadDigitos == 4
	elif dificultad == 3:
	 	cantidadDigitos == 5

	digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	for i in range(cantidadDigitos): 
	 	numeroGenerado = random.choice(digitos)
	 	while numeroGenerado in codigoGenerado:
	 		numeroGenerado = random.choice(digitos)
	 		
	 	codigoGenerado += numeroGenerado
	 	print("número generado: " ,numeroGenerado)

	print("Tienes que adivinar un número de ", cantidadDigitos , "digitos distintos") 
	codigoIngresado = input("¿Qué número propones?:")

	cantidadIntentos = 1

	while codigoIngresado != codigoGenerado:

		cantidadIntentos += 1
		cantidadAciertos = 0
		coincidencias = 0

		for i in range(cantidadDigitos):
			if codigoIngresado[i] == codigoGenerado[i]:
				cantidadAciertos += 1
			elif codigoIngresado[i] in codigoGenerado:
				coincidencias += 1

		print("Tu propuesta fue el número: " , codigoIngresado, "\ntienes: \n" , cantidadAciertos, " aciertos \n", coincidencias, " coincidencias")
		codigoIngresado = input("Propon otro código: ")


	print("Felicidades! adivinaste el número en ", cantidadIntentos , " intentos")
	jugar = int(input("¿Desea seguir jugando?: \n1. Sí \n2. No \n"))


	