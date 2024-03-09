# Crear una matriz 3D para almacenar datos de temperaturas.
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
# Definir el tamaño de la matriz tridimensional (ciudades x días x semanas)
num_ciudades = 4
dias_semana = 7
num_semanas = 4

# Crear una matriz tridimensional con valores de temperaturas (para demostración)
temperaturas = [
    [
        [23, 26, 24, 23, 22, 25, 27],  # Ciudad 1, Semana 1
        [22, 24, 23, 20, 21, 25, 26],  # Ciudad 1, Semana 2
        [26, 27, 28, 26, 24, 23, 21],  # Ciudad 1, Semana 3
        [21, 23, 24, 20, 22, 25, 26],  # Ciudad 1, Semana 4
    ],
    [
        [28, 27, 26, 25, 24, 23, 22],  # Ciudad 2, Semana 1
        [23, 24, 25, 26, 27, 22, 29],  # Ciudad 2, Semana 2
        [22, 21, 23, 23, 25, 26, 27],  # Ciudad 2, Semana 3
        [24, 23, 25, 26, 27, 26, 28],  # Ciudad 2, Semana 4
    ],
    [
        [27, 23, 25, 26, 27, 28, 29],  # Ciudad 3, Semana 1
        [25, 26, 24, 23, 22, 21, 28],  # Ciudad 3, Semana 2
        [26, 24, 25, 27, 26, 28, 27],  # Ciudad 3, Semana 3
        [26, 27, 28, 25, 24, 24, 22],  # Ciudad 3, Semana 4
    ],
    [
        [30, 20, 25, 20, 25, 28, 29],  # Ciudad 4, Semana 1
        [25, 26, 27, 23, 29, 21, 28],  # Ciudad 4, Semana 2
        [24, 22, 25, 21, 26, 20, 23],  # Ciudad 4, Semana 3
        [22, 27, 28, 25, 24, 24, 28],  # Ciudad 4, Semana 4
    ],

]
print(f"::::Temperaturas para cada ciudad y semana::::\n")

#Definimos la funcion
def calcular_prom_ciudad(temp_ciudades):
    num_ciudades = len(temp_ciudades)
    num_semanas = len(temp_ciudades[0])

    promedios_ciudades = []

    for ciudad in range(num_ciudades):
        prom_ciudad = 0

        for semana in range(num_semanas):
            prom_ciudad += sum(temp_ciudades[ciudad][semana])

        prom_ciudad /= (num_semanas * dias_semana)
        promedios_ciudades.append(prom_ciudad)

        print(f"Promedio de temperaturas para la Ciudad {ciudad + 1}: {prom_ciudad:.2f}°C")

    return promedios_ciudades

# Utilizar la función
promedios = calcular_prom_ciudad(temperaturas)