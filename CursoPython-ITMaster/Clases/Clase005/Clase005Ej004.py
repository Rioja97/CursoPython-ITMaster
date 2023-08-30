""" Ejercicio 043

Escribir un programa que lea numeros enteros hasta que se la suma de estos sea mayor que 100,
y muestre la cantidad de numeros ingresados. """

import random

numero = random.randint(1,10)
suma = 0
contador = 0
while (suma < 100):
    contador += 1
    suma += numero

    print(f"Numero: {numero}, Suma: {suma}, cantidad: {contador}")
    numero = random.randint(1,10)

print(f"Cantidad de numeros: {contador}")
