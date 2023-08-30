
def esEntero(cadena):

    try:
        int(cadena)
        return True
    except:
        return False

def leerEnteroEntre(cadena):
    try: 
        int(cadena)
        return True



def leerEntero(cartel):

    datosOk = False

    while datosOk == False:

        cadena = input(cartel)

        if esEntero(cadena):
            numero = int(cadena)
            datosOk = True
           
        else:
            print(f"Error: '{cadena}' no es un número")

    return numero









def main():
    dia = leerEnteroEntre("Dia: ", 1, 31)
    mes = leerEnteroEntre("Mes: ", 1, 12)
    cantPatasPerro = leerEntero("Cuantas patas tiene tu perro?: ")


main()