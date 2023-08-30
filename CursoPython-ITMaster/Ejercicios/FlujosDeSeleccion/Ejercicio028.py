""" Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso que no lo sea. """

import random


ingreso = random.randint(1,12)
""" ingreso = int(input("Ingrese un número: ")) """

mes = ""

if(ingreso == 1): mes = "Enero"
elif(ingreso == 2): mes = "Febrero"
elif(ingreso == 3): mes = "Marzo"
elif(ingreso == 4): mes = "Abril"
elif(ingreso == 5): mes = "Mayo"
elif(ingreso == 6): mes = "Junio"
elif(ingreso == 7): mes = "Julio"
elif(ingreso == 8): mes = "Agosto"
elif(ingreso == 9): mes = "Septiembre"
elif(ingreso == 10): mes = "Octubre"
elif(ingreso == 11): mes = "Noviembre"
elif(ingreso == 12): mes = "Diciembre"
else: print("Error, dato inválido")

print(f"El número {ingreso}, corresponde al mes {mes}")
