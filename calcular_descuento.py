#Crea una función llamada calcular_descuento que tome dos parámetros:
# el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).

def calcular_descuento(monto_total_compra, porc_descuento=10):

    # La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
    descuento = monto_total_compra * (porc_descuento / 100)
    return descuento

# Llamadas a la función calcular_descuento desde el programa principal.
monto_compra = 200.00
#monto_descuento = calcular_descuento(monto_compra)
#monto_final_compra = monto_compra - monto_descuento
#print(f"El monto de esta compra es: ${monto_compra}")
print(f"\n::::::Factura de la compra::::::\n")

monto_compra1 = 400.00
monto_Total = monto_compra + monto_compra1
monto_descuento1 = calcular_descuento(monto_compra + monto_compra1)
monto_final_compra1 = monto_compra1 + monto_compra - monto_descuento1
print(f"El monto Total de esta compra es: ${monto_Total}")
print(f"El descuento de esta compra es: ${monto_descuento1}, \nMonto final a pagar: ${monto_final_compra1}")
print(f"\nGracias por su compra.")