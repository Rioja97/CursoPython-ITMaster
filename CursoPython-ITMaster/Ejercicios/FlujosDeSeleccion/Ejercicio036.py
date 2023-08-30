""" Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). 
Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR'). """


num1 = int(input("Ingrese el primer número: "))
operacion = input("Ingrese la operación, (+), (-), (*), (/): ")
num2 = int(input("Ingrese el segundo número: "))

if(operacion == "+"): print(f"La suma de {num1} y {num2} es: {num1 + num2}")
elif(operacion == "-"): print(f"La resta de {num1} y {num2} es: {num1 - num2}")
elif(operacion == "*"): print(f"La multiplicación de {num1} por {num2} es: {num1 * num2}")
elif(operacion == "/"): 
    if(num1 == 0 and num2 == 0): print(f"ERROR. No se puede dividir {num1} por {num2}")
    else: print(f"La división de {num1} por {num2} es: {num1 / num2}")
else: print("ERROR. Caracter inválido. Recuerde ingresar alguno de estos caracteres: (+), (-), (*), (/)")