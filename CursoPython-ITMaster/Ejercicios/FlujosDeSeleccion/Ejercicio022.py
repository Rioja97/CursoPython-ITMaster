""" Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor. """

while(True):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    num3 = int(input("Ingrese otro número: "))

    print(f"El número mas grande es: {max(num1, num2, num3)}")