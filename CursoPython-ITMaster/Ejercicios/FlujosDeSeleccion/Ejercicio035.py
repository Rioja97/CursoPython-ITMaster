""" Existen dos reglas que identifican dos conjuntos de valores:

a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.

Debe asignar el valor que corresponda a las variables booleanas:

esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. 
Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados. """

numero = int(input("Ingrese un número: "))

unDigito = numero > 0 and numero < 10
impar = not(numero % 2 == 0)
estaEnAmbos = unDigito and impar
noEstaEnNinguno = unDigito and impar

if(unDigito and impar): print("El numero esta en la categoria de impar y de un digito")
elif(not unDigito and impar): print("El número es de más de un dígito e impar")
elif(not unDigito and  not impar): print("El número es de más de un dígito y par")
elif(unDigito and not impar): print("El número es de un dígito y par")
else: print("El numero no pertenece a ninguna categoría")