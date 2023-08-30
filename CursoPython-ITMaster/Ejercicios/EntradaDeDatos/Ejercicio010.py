#Escribir un programa para resolver el siguiente problema:

#Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). 
# Calcular qué porcentaje invirtió cada una.

p1 = int(input("Ingrese la cantidad de dinero de la persona 1: "))
p2 = int(input("Ingrese la cantidad de dinero de la persona 2: "))
p3 = int(input("Ingrese la cantidad de dinero de la persona 3: "))

total = p1 + p2 + p3

porcP1 = round((p1 / total) * 100, 2)
porcP2 = round((p2 / total) * 100, 2)
porcP3 = round((p3 / total) * 100, 2)

print(f"La persona 1 ha invertido {porcP1}%")
print(f"La persona 2 ha invertido {porcP2}%")
print(f"La persona 3 ha invertido {porcP3}%")