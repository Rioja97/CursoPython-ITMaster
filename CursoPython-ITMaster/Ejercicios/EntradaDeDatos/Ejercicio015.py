""" Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, 
más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran? """

base = 200000
comisionFija = 15000
nombreVendedor = input("Ingrese el nombre del vendedor: ")
cantidadVentas = int(input("Ingrese la cantidad de ventas del vededor: "))
ventasVendedor = int(input("Ingrese el total de las ventas del vendedor: "))
comisionVentas = round(ventasVendedor * 5) / 100
sueldoVendedor = base + comisionFija + (comisionVentas * 347)

print(f"EL sueldo total de {nombreVendedor} en el mes es de: ${sueldoVendedor}")