""" Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse. """

""" while(True):
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    genero = input("Ingrese el género de la persona: ").upper()

    if(edad < 1 or edad > 120 or genero != "MASCULINO" or genero != "FEMENINO"):
        print(f"La persona: {nombre} no ha ingresado correctamente los datos")
    else:
        if(genero == "FEMENINO" and edad >= 60):
            print(f"La persona {nombre}, está en edad de jubilarse")
        elif(genero == "MASCULINO" and edad >= 65):
            print(f"La persona {nombre}, está en edad de jubilarse")
        else:
            print(f"La persona {nombre}, no está en edad de jubilarse")
 """
while True:
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    genero = input("Ingrese el género de la persona: ").upper()

    if edad < 1 or edad > 120:
        print(f"La persona {nombre} no ha ingresado correctamente la edad")
    elif genero != "MASCULINO" and genero != "FEMENINO":
        print(f"La persona {nombre} no ha ingresado correctamente el género")
    else:
        if genero == "FEMENINO" and edad >= 60:
            print(f"La persona {nombre}, está en edad de jubilarse")
        elif genero == "MASCULINO" and edad >= 65:
            print(f"La persona {nombre}, está en edad de jubilarse")
        else:
            print(f"La persona {nombre}, no está en edad de jubilarse")