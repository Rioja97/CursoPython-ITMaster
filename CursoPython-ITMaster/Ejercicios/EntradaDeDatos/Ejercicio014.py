""" Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el valor del metro cuadrado de tierra. 
El programa debe calcular y mostrar el valor total del terreno. 
Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno a tres alturas distintas.

Pensando los pasos para resolver el problema:
Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable. Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable.
Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable. 
Calcular el valor total del terreno multiplicando el ancho por el largo y luego multiplicando el resultado por el valor del metro cuadrado de tierra.
Mostrar el valor total del terreno al usuario.
Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. 
Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura, a 2 metros de altura y a 3 metros de altura. 
Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) y luego multiplicarlo por la cantidad de alturas. 
Mostrar la cantidad de metros de alambre necesarios para cercar el terreno a las tres alturas distintas al usuario. """

ancho = int(input("Ingrese el valor del ancho del terreno: "))
largo = int(input("Ingrese el valor del largo del terreno: "))
m2 = int(input("Ingrese el valor del metro cuadrado del terreno: "))
total = (ancho * largo) * m2
mAlambre = (ancho * 2) + (largo * 2) * 3


print(f"El valor total del terreno es de ${total}, siendo ${m2} el valor del metro cuadrado.")
print(f"La cantidad de alambre necesaria es de {mAlambre} metros")