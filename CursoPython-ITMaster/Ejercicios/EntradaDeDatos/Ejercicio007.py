#Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:

#a. Multiplicado por 10. (utilizar el operador *) a. Dividido por 10. (utilizar el operador /) a. Elevado al cuadrado. (utilizar el operador **)

#Cada resultado debe mostrarse en una línea distinta.

num = int(input("Ingrese un número: "))

mult = num * 10
div = num / 10
pot = num ** 2

print(f"{num} * 10 = {mult}")
print(f"{num} / 10 = {div}")
print(f"{num} ** 2 = {pot}")