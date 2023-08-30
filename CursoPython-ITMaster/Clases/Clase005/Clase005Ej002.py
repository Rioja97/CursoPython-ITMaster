suma = 0
cantidad = 10
for contador in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el {contador} de {cantidad} números: "))
    suma += numero

print(f"La suma total es de: {suma}")