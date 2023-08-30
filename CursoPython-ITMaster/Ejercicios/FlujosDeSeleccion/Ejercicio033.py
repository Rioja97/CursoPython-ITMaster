""" La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios. """

from random import randint

compra = randint(500, 20000)

descuentoMenor = (compra * 0.955)
descuentoMedio = (compra * 0.92)
descuentoMayor = (compra * 0.895)

if(compra < 5500): print(f"La compra de ${compra}, con el descuento aplicado, queda en un total de: ${descuentoMenor}")
elif(compra >= 5500 and compra < 10000): print(f"La compra de ${compra}, con el descuento aplicado, queda en un total de: ${descuentoMedio}")
else: print(f"La compra de ${compra}, con el descuento aplicado, queda en un total de: ${descuentoMayor}")

