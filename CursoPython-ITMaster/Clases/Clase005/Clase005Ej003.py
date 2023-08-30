maximo = float("-inf")
numero = int(input("Numero: "))
minimo = float("inf")
hayDatos = False
while numero != 0:
    hayDatos = True
    if (numero > maximo):
        maximo = numero

    if(numero < minimo):
        minimo = numero

    numero = int(input("Numero: "))

if (hayDatos):
    print(f"Maximo = {maximo}")
    print(f"Minimo = {minimo}")
else: print("No se ingresaron datos")