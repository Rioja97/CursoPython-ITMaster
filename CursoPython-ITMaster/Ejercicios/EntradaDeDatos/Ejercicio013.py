""" Escribir un programa para calcular el importe a cobrar por un vendedor, considerando su sueldo fijo de $200.000 pesos más el 16% del monto total de ventas realizadas durante un mes.

Pensando los pasos para resolver el problema:
Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.

Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

Mostrar el importe a cobrar por el vendedor.

Para pensar:
¿Qué pasaría si se modificara el sueldo fijo del vendedor?

Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para calcular el salario total debería ser actualizada para reflejar el nuevo sueldo fijo. 
En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría. De igual manera, si el sueldo fijo disminuye, entonces el salario total también disminuiría. 
Es importante actualizar la fórmula en el programa para asegurarse de que el cálculo del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.

¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono? """

ventasVendedor = int(input("Ingrese las ventas del vendedor en el mes: "))
porc16 = round((ventasVendedor * 16 / 100), 2)
sueldoBasico = int(input("Ingrese el sueldo básico del vendedor: "))
sueldoTotal = sueldoBasico  + porc16

print(f"El salario total del vendedor es de: ${sueldoTotal}, contando el salario básico de ${sueldoBasico} y el 16% de las ventas con un total de ${porc16}")
