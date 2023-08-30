""" Ejercicio 349 """

opcion = input("Continua? [S/N]: ").upper()
while opcion not in ('S', 'N'): 
    print(f"{opcion} no es válida!")
    opcion = input("Continua? [S/N]: ").upper()
print(opcion)