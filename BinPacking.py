import random
import numpy as np

def sortNonIncreising(array):
	for i in range(1,len(array)):
		key = array[i]
		j = i-1
		while j >= 0 and key > array[j]:
			array[j+1] = array[j]
			j -=1
		array[j+1] = key	

print("Ingrese el nombre del archivo: ")
print("En caso que no asigne ningun nombre, generare numeros aleatorios.")
arg = input()
if (arg == "Archivo.txt"):
	archivo = open("Archivo.txt", "r")
	for linea in archivo.readlines():
		print(linea)
		numeros = linea
		numeros = numeros.split(',')
		print(numeros)
		x = np.array(numeros)
		y = astype(np.float)
		print(y)
		"""for x in numeros:
			flotantes = float(x)
			print(flotantes)
			lista = []
			lista.append(flotantes)
			print(lista)"""
	archivo.close()
else:
		print("Se va a generar una lista de numeros al azar: ")	
		desde = .01
		hasta = .99
		cantidad = 20
		numero = [random.uniform(desde,hasta) for x in range(cantidad)]
		for i in range(len(numero)):
			print("%f" % numero[i])