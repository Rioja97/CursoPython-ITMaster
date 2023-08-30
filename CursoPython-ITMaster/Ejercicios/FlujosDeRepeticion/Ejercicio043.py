""" Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados. """

from random import randint

numero = randint(1, 10)
suma = 0
contador = 0

while suma < 100:
    suma += numero
    contador += 1
    print(f"Numero {numero}, suma {suma} y contador {contador}")
    numero = randint(1, 10)

print(f"El total de números sumados es de: {contador} y la suma es de: {suma}")