""" Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje. """

from random import randint

cantKilometros = randint(0, 25)
tarifa = 50
precioPocoKilometro = (cantKilometros * 20)
precioMuchoKilometro = (cantKilometros * 15)

if(cantKilometros <= 10): tarifa += precioPocoKilometro
else: tarifa += precioMuchoKilometro

print(f"El costo del viaje de {cantKilometros} kilómetros, será de ${tarifa}")