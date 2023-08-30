""" Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener al menos 10 años de edad y medir más de 1,60 metros.
(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)

Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. 
Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, 
el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad,
el programa debe imprimir "Lo siento, eres demasiado joven para acceder." Si no cumple con el requisito de la estatura, 
el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"
Los conectores lógicos "and" y "or" son operadores booleanos utilizados en programación y en lógica matemática para combinar o unir dos o más expresiones lógicas.

El conector "and" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. 
La expresión completa es verdadera sólo si todas las expresiones individuales son verdaderas. 
Por ejemplo, la expresión lógica "A and B" será verdadera sólo si tanto A como B son verdaderos. Si alguna de las expresiones es falsa, la expresión completa será falsa.

La tabla de verdad del operador "and" se utiliza en lógica proposicional para determinar el valor de verdad de una proposición compuesta 
formada por dos proposiciones simples unidas por "and". La tabla de verdad del "and" se construye evaluando todas las posibles combinaciones 
de valores de verdad de las proposiciones simples, y determinando el valor de verdad de la proposición compuesta para cada combinación. """

while(True):
    edad = int(input("Ingrese la edad de la persona: "))
    altura = float(input("Ingrese la altura de la persona: "))

    if(edad >= 10):
        if(altura >= 1.60):
            print("Bienvenido, puede pasar!")
        else: 
            print("Lo siento, no tiene la altura suficiente para entrar")
    elif(edad < 10 and altura < 1.60):
        print("Lo siento, no tiene la edad ni la altura suficiente para entrar")
    else:
        print("Lo siento, no tiene la edad suficiente para entrar")