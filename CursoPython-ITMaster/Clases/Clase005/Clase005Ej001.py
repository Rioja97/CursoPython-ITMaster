""" Leer numeros hasta que se ingrese un cero. Mostrar la suma

lista1 ==> 2,1,6,7,1,4,5,2,6,4,2,1,4,5,0
lista2 ==> 2,1,6,7,1,4,5,2,6,4,0
lista3 ==> 2,1,6,7,1,4,0
lista4 ==> 0

"""
suma = 0
numero = int(input("Ingrese un numero: "))

while (numero != 0):
    suma += numero 
    numero = int(input("Ingrese un numero: "))

print(f"La suma total es: {suma}")