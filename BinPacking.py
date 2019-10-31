import random

def sortNonIncreising(array):
	for i in range(1,len(array)):
		key = array[i]
		j = i-1
		while j >= 0 and key > array[j]:
			array[j+1] = array[j]
			j -=1
		array[j+1] = key	

print("Ingrese el nombre del archivo: ")
print("En caso de que quiera generar numeros aleatorios, presione 2.")
arg = input()
if (arg == "Archivo.txt"):
	archivo = open("Archivo.txt", "r")
	for linea in archivo.readlines():
		print(linea)
		numeros = linea
		numeros = numeros.split(',')
		print(numeros)
		"""for x in numeros:
			flotantes = float(x)
			print(flotantes)
			lista = []
			lista.append(flotantes)
			print(lista)"""
	archivo.close()
elif (arg == 2):
		print("Se va a generar una lista de numeros al azar: ")	
		desde = .01
		hasta = .99
		cantidad = 20
		#Genera los numeros aleatorios
		numero = [random.uniform(desde,hasta) for x in range(cantidad)]
		#Ordenamos la lista con los numeros al azar
		print("Lista ordenada de mayor a menor: ")
		#Primer paso del algoritmo
		sortNonIncreising(numero)
		#Esta es la lista en la manera en como quedo ordenado
		print(numero)
		#Numero de items
		n = len(numero)
		print("Numero de items: ")
		print(n)
		#Capacidad limite de los bins
		c = 1
		float(c)
		#Array de bins
		bins = []
		for i in numero:
			bins.append(i)
		#Indice i
		i = 0
		int(i)
		#numero de bins
		num_bins = 0
		int(num_bins)
		#Algoritmo de Neapolitan & Naimipour
		#There are still unpacked items
		while(i < n):
			#Indice j
			j = 0
			#get next item
			#the item is not packed and there are more started bins
			while(j < num_bins):
				#get next bin
				#the item fits in the bin
				if(bins[j] >= numero[i]):
					#pack it in the bin
					bins[j] = bins[j] - numero[i]
					break
			#the item is not packed
				j += 1
			if(j == num_bins):
				#start a new bin
				bins[num_bins] = c - numero[i]
				num_bins += 1
				#place the item in the new bin
			i += 1
		print("Numero aproximado de bins que se obtendrian: ")
		print(num_bins)
		#Opt sera el numero optimo de bins dado de un ejemplar
		"""for i in range(len(numero)):
			print("%f" % numero[i])"""
else:
	print("Ingrese un comando valido")
