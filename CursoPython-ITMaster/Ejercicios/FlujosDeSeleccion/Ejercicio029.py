""" Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. 
Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4. """

notaValida = range(1, 11)
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
promedio = (nota1 + nota2) / 2

if(nota1 and nota2) >= 1 and (nota1 and nota2) <= 10:
    if(promedio >= 7):
        print("Felitaciones! Usted ha promocionado!")
    elif(promedio >= 4):
        print("Bien hecho, usted ha aprobado")
    else:
        print("Suerte la próxima, usted ha reprobado")
else: print("Alguna de las notas ingresadas no son válidas. Recuerde ingresar una nota entre 1 y 10")


""" (nota1 >= 1 and nota1 <=10) and (nota2 >= 1 and nota2 <= 10) """