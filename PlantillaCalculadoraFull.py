#------------------------PlantillaCalculadoraFull---------------------\\
# 23/09/2021
# Santiago, Chile
# Eddie Casañas
# JAVA PORT
# Permite que se puedan hacer operaciones con mas de dos numeros
#---------------------------------------------------------------------\\

import GenerarListaNumericaPlantilla as g
obj = g.generarListaNumerica

class Calculadora:
	def suma(self):
		print("SUMA")
		resultado = ""
		numeros = obj.devuelveLista(self)
		for i in range(len(numeros)):
			if i == len(numeros) - 1:
				num = str(numeros[i]) + " = "
				resultado += num
			else:
				num = str(numeros[i]) + " + "
				resultado += num
				
		print("\n" + resultado + str(sum(numeros)))
		
	def resta(self):
		print("RESTA")
		resultado = ""
		numeros = obj.devuelveLista(self)
		resta = numeros[0]
		resultado += str(resta) + " - "
		for i in range(1, len(numeros)):
			if i == len(numeros) - 1:
				resultado += str(numeros[i]) + " = "
				resta -= numeros[i]
			else:
				resultado += str(numeros[i]) + " - "
				resta -= numeros[i]
				
		print("\n" + resultado + str(resta))
		
	def multiplicacion(self):
		print("MULTIPLICACION")
		resultado = ""
		multiplicacion = 1
		numeros = obj.devuelveLista(self)
		for i in range(len(numeros)):
			if i == len(numeros) - 1:
				resultado += str(numeros[i]) + " = "
				multiplicacion *= numeros[i]
			else:
				resultado += str(numeros[i]) + " * "
				multiplicacion *= numeros[i]
				
		print("\n" + resultado + str(multiplicacion))
		
	def division(self):
		print("DIVISION")
		resultado = ""
		#USAR EL devuelveLista2, QUE ES ESPECIFICO PARA DIVISIONES
		numeros = obj.devuelveLista2(self)
		division = numeros[0]
		resultado += str(numeros[0]) + " / "
		for i in range(1, len(numeros)):
			if i == len(numeros) - 1:
				resultado += str(numeros[i]) + " = "
				division /= numeros[i]
			else:
				resultado += str(numeros[i]) + " / "
				division /= numeros[i]
				
		print("\n" + resultado + str(division))
		
	def exponente(self):
		while True:
			print("EXPONENTE")
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")
				continue
			print("Ingrese el exponente: ")
			try:
				exponente = float(input())
				resultado = (numero1 ** exponente)
				print("\n" + str(numero1) + " ^ " + str(exponente) 
				+ " = " + str(resultado))
				break
			except:
				print("\nIngrese un numero valido")
				
	def raizCuadrada(self):
		while True:
			print("RAIZ CUADRADA")
			print("\nIngrese el numero: ")
			try:
				numero = float(input())
				if numero < 0:
					print("\nIngrese solo numeros positivos\n")
					continue
			except:
				print("\nIngrese un numero valido\n")
				continue
			try:
				raiz = numero ** (1/2)
				print("\nLa raiz cuadrada de " + str(numero) + " es: " 
				+ str(raiz))
				break
			except:
				print("\nError en el calculo")
				
	def repetir():
		while True:
			print("\n(1): Repetir")
			print("(2): Volver al menu principal")
			opcion = input()
			if opcion.strip() != "1" and opcion.strip() != "2":
				print("\nIngrese una opcion valida")
				continue
			elif opcion.strip() == "1":
				return 1
			elif opcion.strip() == "2":
				return 2
		
				

		
