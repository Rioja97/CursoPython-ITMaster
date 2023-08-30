""" Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. 
Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. 
Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. 
Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."

Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados? """

angulo1 = int(input("Ingrese el valor del primer ángulo: "))
angulo2 = int(input("Ingrese el valor del segundo ángulo: "))

total = 180

suma = angulo1 + angulo2
angulo3 = (total - angulo1 - angulo2)

if(angulo1 < 0 or angulo2 < 0):
    print("No mostro, ingresá un número mayor a 0.")
else :
    if(suma > 179):
        print("No mostro, no entendiste nada. Los angulos no pueden ser mayores a 179.")
    else:
        print(f"El valor del angulo restante es: {angulo3}")

