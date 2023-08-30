""" Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b. """

a = int(input("Ingrese un mínimo: "))
b = int(input("Ingrese un máximo: "))



sumaPares = 0
productoImpares = 1
numerosSumados = ''
numerosMultiplicados = ''


for x in range(a, b+1):
    
    if (x % 2 == 0): 
        sumaPares += x
        numerosSumados += f"{x}, "
    else: 
        numerosMultiplicados += f"{x}, "
        productoImpares = productoImpares * x

print(f"Numeros pares: [{numerosSumados}]")
print(f"La suma de pares entre {a} y {b} es de: {sumaPares}")
print(f"Numeros impares: [{numerosMultiplicados}]")
print(f"El producto de impares entre {a} y {b} es de: {productoImpares}")
        