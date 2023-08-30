"""
Ejercicio 041

Escribir un programa que lea números enteros hasta que se 
ingrese un 0, y muestre el máximo.
"""

maximo = float("-inf")
minimo = float("inf")

numero = int(input("Ingrese un número: "))
hayDato = False

while numero != 0:
    hayDato = True

    if(numero > maximo):
        maximo = numero
    
    if (numero < minimo):
        minimo = numero
        
    numero = int(input("Ingrese un número: "))

if(hayDato):
    print(f"El número máximo es: {maximo}")
    print(f"El número mínimo es: {minimo}")
else: 
    print("No se han ingresado datos")