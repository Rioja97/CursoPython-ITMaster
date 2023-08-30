#Escribir un programa que permita resolver el siguiente problema:

#Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

#Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

persona1 = int(input("Ingrese lo aportado por persona 1: "))
persona2 = int(input("Ingrese lo aportado por persona 2: "))
persona3 = int(input("Ingrese lo aportado por persona 3: "))

total = persona1 + persona2 + persona3

porc1 = round((persona1 / total) * 100, 2)
porc2 =  round((persona2 / total) * 100, 2) 
porc3 =  round((persona3 / total) * 102, 2)

print(f"La persona 1, aportó ${persona1} relativo al {porc1}%")
print(f"La persona 2, aportó ${persona2} relativo al {porc2}%")
print(f"La persona 3, aportó ${persona3} relativo al {porc3}%")
print(f"El total recaudado es de: ${total}")