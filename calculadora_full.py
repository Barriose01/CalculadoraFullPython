#------------------------CALCULADORA FULL-----------------------------\\
# 23/09/2021
# Santiago, Chile
# Eddie Casañas
# JAVA PORT
# SE PUEDEN HACER OPERACIONES CON MAS DE DOS NUMEROS
#---------------------------------------------------------------------\\

import PlantillaCalculadoraFull as p
obj = p.Calculadora

salida = 0
while salida != 7:
	print("CALCULADORA FULL")
	while True:
		print("\n(1): Suma")
		print("(2): Resta")
		print("(3): Multiplicacion")
		print("(4): Division")
		print("(5): Exponente")
		print("(6): Raiz cuadrada")
		print("(7): Salir")
		
		try:
			opcion = int(input())
			if opcion < 1 or opcion > 7:
				print("\nIngrese una opcion valida\n")
				continue
			else:
				break
		except:
			print("\nIngrese una opcion valida\n")
			continue
			
	if opcion == 1:
		salida = 0
		while salida != 2:
			obj.suma(obj)
			salida = obj.repetir()
				
	elif opcion == 2:
		salida = 0
		while salida != 2:
			obj.resta(obj)
			salida = obj.repetir()
				
	elif opcion == 3:
		salida = 0
		while salida != 2:
			obj.multiplicacion(obj)
			salida = obj.repetir()
				
	elif opcion == 4:
		salida = 0
		while salida != 2:
			obj.division(obj)
			salida = obj.repetir()
				
	elif opcion == 5:
		salida = 0
		while salida != 2:
			obj.exponente(obj)
			salida = obj.repetir()
				
	elif opcion == 6:
		salida = 0
		while salida != 2:
			obj.raizCuadrada(obj)
			salida = obj.repetir()
				
	elif opcion == 7:
		salida = 7
