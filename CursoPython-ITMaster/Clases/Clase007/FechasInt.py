def elDia(aaaammdd):
    return aaaammdd % 100


def elMes(aaaammdd):
    return (aaaammdd // 100) % 100


def elAnio(aaaammdd):
    return aaaammdd // 10000


def strFecha(aaaammdd):
    return f"{elDia(aaaammdd) :02}/{elMes(aaaammdd) :02}/{elAnio(aaaammdd) :04}"

def esBisiesto(anio):
    return anio % 4 == 0


def obtenerCantidadDiasMes(mes, anio):
    dias = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# index     0  1   2   3   4   5   6   7   8   9   10  11  12
    if mes == 2 and esBisiesto(anio):
        return 29
    
    return dias[mes]


def esFechaValida(aaaammdd):
    anio = elAnio(aaaammdd)
    if anio < 1:
        return False
    
    mes = elMes(aaaammdd)
    if mes < 1 or mes > 12:
        return False
    
    dia = elDia(aaaammdd)
    if (dia < 1 or dia > obtenerCantidadDiasMes(mes, anio)):
        return False
    
    return True

def main():
    fecha = int(input("Ingrese una fecha en formato AAAAMMDD: ")) #AAAAMMDD

    if esFechaValida(fecha):
        print(strFecha(fecha))
    else: print(f"La fecha {fecha} no es una fecha válida!")

main()


