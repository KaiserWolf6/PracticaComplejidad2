import random


def sortNonIncreising(array):
	for i in range(1,len(array)):
		key = array[i]
		j = i-1
		while j >= 0 and key > array[j]:
			array[j+1] = array[j]
			j -=1
		array[j+1] = key

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
import random
 
def aleatorios(cantidad, min, max):
    numeros = set()
 
    if max < min:
        min, max = max, min
 
    if cantidad > (max-min):
        print ("solamente puedo generar %d numeros" % (max-min))
        cantidad = max - min
 
    while len(numeros) < cantidad:
        numeros.add(random.uniform(min, max))
 
    return numeros

print("Escribe algo")
var = input()
if (var == "Archivo.txt"):
	pass
else:
		print("Se va a generar numeros al azar")	

# Driver code to test above 
arr = [0.88, .03, 0.55, .05, .96] 

sortNonIncreising(arr) 	
for i in range(len(arr)): 
    print ("%g" % arr[i])


desde = .01
hasta = .99
cantidad = 20
numero = [random.uniform(desde,hasta) for x in range(cantidad)]
for i in range(len(numero)):
	print("%f" % numero[i])

print(aleatorios(cantidad,desde,hasta))    