""" Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0) """

from random import randint

num1 = randint(0, 100)
num2 = randint(0, 100)

if(num1 % num2 == 0): print(f"Los numeros {num1} y {num2} son divisibles")
else: print(f"Los numeros {num1} y {num2} no son divisibles")
