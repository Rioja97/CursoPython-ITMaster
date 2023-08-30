#Escribir un programa que permita ingresar el valor monetario de una hora de trabajo 
# y la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador 
# que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, 
# suponiendo que todas las horas tienen el mismo valor.

valorHora = int(input("Ingrese el valor de una hora de trabajo: "))
cantHoras = int(input("Ingrese la cantidad de horas trabajadas en el día: "))

salDiario = valorHora * cantHoras
salHabil = salDiario * 5
salSabado = (salDiario / 2)

salSemanal = salHabil + salSabado

print(f"El salario semanal es: {salSemanal}")

