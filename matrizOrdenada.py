#Escribe un programa que incluya una matriz bidimensional con valores numéricos
#(puede ser una matriz pequeña de 3x3).

# Definir una matriz de 3x3
matriz = [
    [3, 1, 4],
    [52, 1, 9],
    [2, 6, 5]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Especificar la fila que se desea ordenar (en este caso, la fila 1)
numero_fila_ordenar = 1

# Ordenar la fila seleccionada utilizando Bubble Sort
fila_ordenar = matriz[numero_fila_ordenar]
n = len(fila_ordenar)

for i in range(n):
    for j in range(0, n-i-1):
        if fila_ordenar[j] > fila_ordenar[j+1]:
            fila_ordenar[j], fila_ordenar[j+1] = fila_ordenar[j+1], fila_ordenar[j]

# Mostrar la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in matriz:
    print(fila)
