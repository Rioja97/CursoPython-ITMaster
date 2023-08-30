#Escribir un programa que solicite al usuario ingresar tres notas de un alumno. 
# El programa debe mostrar por pantalla las notas separadas por comas 
# en un renglón y el promedio de las notas en el siguiente renglon.

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

prom = (nota1 + nota2 + nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"El promedio es: {prom}")