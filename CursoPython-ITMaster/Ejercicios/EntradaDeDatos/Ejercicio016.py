""" Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. 
Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. 
El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos. Usar en el programa las siguientes instrucciones: """

tiempoEnSegundos = int(input("Ingrese un período de tiempo en segundos: "))
segundosRestantes = tiempoEnSegundos % 60
minuto = (tiempoEnSegundos % 3600)  // 60
hora = (tiempoEnSegundos % 86400)  // 3600
dia = tiempoEnSegundos // 86400

print(f"{tiempoEnSegundos} segundos equivale a {dia} dias, {hora} horas, {minuto} minutos y {segundosRestantes} segundos")