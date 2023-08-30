""" Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo. """


while(True):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))

    if(num1 > num2): print("El primer número es mayor al segundo")

    elif(num1 == num2): print("Los números son iguales")
    
    else: print("El primer número es menor al segundo")