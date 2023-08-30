""" Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que esta en medio.

Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor, el número 7 como el mayor y el número 3 como el que esta en medio.

Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas? """


while(True):
    uno = int(input("Ingrese el primer número: "))
    dos = int(input("Ingrese el segundo número: "))
    tres = int(input("Ingrese el tercer número: "))

    if(uno > dos and uno > tres and dos > tres): 
        mayor = uno
        medio = dos
        menor = tres
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    elif(uno > dos and uno > tres and dos < tres): 
        mayor = uno
        medio = tres
        menor = dos
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    elif(uno < dos and uno < tres and dos > tres): 
        mayor = dos
        medio = tres
        menor = uno
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    elif(uno < dos and uno > tres and dos > tres): 
        mayor = dos
        medio = uno
        menor = tres
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    elif(uno < dos and uno < tres and dos < tres): 
        mayor = tres
        medio = dos
        menor = uno
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    elif(uno > dos and uno < tres and dos < tres): 
        mayor = tres
        medio = uno
        menor = dos
        print(f"El número mayor es: {mayor}, el del medio es: {medio} y el menor es {menor}")

    else:
        print("Los números son iguales perrito malvado")
        

    