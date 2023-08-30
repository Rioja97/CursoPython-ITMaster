""" Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse. """

invitados = int(input("Indique la cantidad de invitados a la fiesta: "))
asientosDisponibles = int(input("Indique la cantidad de asientos dispoibles en el salón: "))

faltantes = invitados - asientosDisponibles

if(invitados > asientosDisponibles):
    print(f"La cantidad de invitados supera la cantidad de asientos disponibles. Faltan {faltantes} asientos para los invitados")
else: 
    print("Los asientos disponibles alcanzan para la cantidad de invitados")