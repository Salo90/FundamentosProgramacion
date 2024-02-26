#Escribe un programa que incluya una matriz bidimensional,
# (puede ser una matriz pequeña de 3x3) con valores numéricos.

Edades = [
     [6,56,8],
     [15,5,81],
     [61,51,18]
]

# Buscar un valor especifico en la matriz
valor_buscado = 51
# Inicializacion de variables para rastrear la posicion del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor deseado
for fila in range(len(Edades)):
    for columna in range(len(Edades[fila])):
        if Edades[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break # Detener la busqueda una vez hallada el valor
    if fila_encontrada != -1:
        break # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontro el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontro {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"{valor_buscado} no se encontro en la matriz.")