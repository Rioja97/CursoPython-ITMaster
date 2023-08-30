""" Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados. """

numero = int(input("Ingrese un número: "))
hayDato = False
contador = 0
numeros = 0
promedio = 0

while numero != 0:
    
    hayDato = True
    contador += 1
    numeros += numero
    numero = int(input("Ingrese un número: "))

promedio = (numeros / contador)

if(hayDato):
    print(f"El promedio de los números ingresados es de: {round(promedio, 2)}")
else: print("No se ha ingresado ningún dato")
