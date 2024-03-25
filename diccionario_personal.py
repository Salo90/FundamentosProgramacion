#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona,
# incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

print(f"\n::::Información Persopnal::::\n")
informacion_personal = {"Nombre":"Jose", "Edad":20 , "Ciudad":"Tena" }

#Accede al valor asociado con la clave y la modifica.
informacion_personal["Ciudad"] = "Quito"

#Agrega una nueva clave-valor
informacion_personal["Profesión"] = "Peluquero"

#Verifica si la clave telefono existe en el diccionario,
# si no existe, la agrega con un número de teléfono ficticio.
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = 959685214

#Elimina una clave y valor.
del (informacion_personal["Edad"])

#Imprime el diccionario resultante
print(informacion_personal)