#Bucle While 
#Definimos funcion para imprimir arreglos
def imprimir_arreglos(arreglo):
  i = 0
  while (i in range(len(arreglo))):
    print(f'[{arreglo[i]}]', end = "")
    i += 1

#Definimos funcion para ordenar, por Burbuja, los elementos de la lista
def algoritmo_burbuja(arreglo):
  i = 0
  while(i in range(len(arreglo))):
    i += 1 
    j = 0
    while(j in range(len(arreglo)-i)):
      if arreglo[j] > arreglo[j+1]:
        aux = arreglo[j]
        arreglo[j] = arreglo[j+1]
        arreglo[j+1] = aux
      j+=1
    
#Definimos el arreglo ejemplo
lista_sueldos = [20.8, 150.5, 170.5, 180.8, 190, 30, 75.6, 200]

#Imprimimos el algoritmo original
print("\nAlgoritmo Original:")
imprimir_arreglos(lista_sueldos)

#Pasamos el algoritmo
algoritmo_burbuja(lista_sueldos)

#Imprimimos el arreglo ordenado por burbuja
print("\n\nAlgoritmo Arreglado por Burbuja:")
imprimir_arreglos(lista_sueldos)