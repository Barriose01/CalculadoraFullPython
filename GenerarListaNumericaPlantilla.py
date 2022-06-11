#------------------------Generar Lista Numerica----------------------\\
# 19/09/2021
# Santiago, Chile
# Eddie Casañas
# JAVA PORT
# Usado con las calculadoras
# Permite que se puedan hacer operaciones con mas de dos numeros
#---------------------------------------------------------------------\\

class generarListaNumerica:
	def devuelveLista(self):
		while True:
			print("\nIngrese la cantidad con la que desea trabajar: ")
			try:
				cantidad = int(input())
				if cantidad < 0:
					print("\nIngrese una cantidad valida")
					continue
				if cantidad < 2:
					print("\nIngrese un minimo de dos numeros")
					continue
			except:
				print("\nIngrese un valor apropiado")
				continue
				
			i = 0
			lista_numeros = []
			
			for x in range(cantidad):
				lista_numeros.append(0)
				
			while i < cantidad:
				print("\nIngrese un numero: (" + str(i+1) + ")")
				try:
					numero = float(input())
					lista_numeros[i] = numero
				except:
					print("\nIngrese un numero valido")
					continue
				i+= 1
			return lista_numeros
	
	
	#USADO PARA OBTENER UNA LISTA DE NUMEROS AL TRABAJAR CON DIVISIONES
	def devuelveLista2(self):
		while True:
			print("\nIngrese la cantidad con la que desea trabajar: ")
			try:
				cantidad = int(input())
				if cantidad < 0:
					print("\nIngrese una cantidad valida")
					continue
				if cantidad < 2:
					print("\nIngrese un minimo de dos numeros")
					continue
			except:
				print("\nIngrese un valor apropiado")
				continue
				
			i = 0
			lista_numeros = []
			
			for x in range(cantidad):
				lista_numeros.append(0)
				
			while i < cantidad:
				print("Ingrese el numero: (" + (str(i + 1)) + ")")
				try:
					numero = float(input())
					if i != 0 and numero == 0.0:
						print("\nIngrese numeros distintos de 0")
						continue
					else:
						lista_numeros[i] = numero
					i += 1
				except:
					print("\nIngrese un numero valido")
					continue
			
			return lista_numeros
						
