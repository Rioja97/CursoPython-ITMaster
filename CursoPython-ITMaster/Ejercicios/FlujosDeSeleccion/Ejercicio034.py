""" Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. 
Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, 
mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

Jubilación: 11%

Obra Social: 3%

Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

Jubilación - 999,99

Obra Social - 999,99

Sindicato - 999,99

Sueldo Neto 999,99

 """

nombreEmpleado = input("Ingrese el nombre del empleado: ")
sueldoBasico = int(input(f"Ingrese el sueldo básico de {nombreEmpleado}: "))
aniosDeAntiguedad = int(input(f"Ingrese los años de antiguedad de {nombreEmpleado}: "))
estadoCivil = input(f"Ingrese el estado civil de {nombreEmpleado}: ")
estadoCivilOk = (estadoCivil == "Soltero") or (estadoCivil == "Casado")

jubilacion = (sueldoBasico * 11) / 100
obraSocial = (sueldoBasico * 3) / 100
sindicato = (sueldoBasico * 3) / 100
salarioBruto = sueldoBasico - jubilacion - obraSocial - sindicato
soltero = salarioBruto + (aniosDeAntiguedad * ((salarioBruto * 5)/100))
casado = salarioBruto + (aniosDeAntiguedad * ((salarioBruto * 7)/100))

sueldoTotal = 0

if(not estadoCivilOk): print("Ingrese un estado civil válido") 
else:
    if (estadoCivilOk == "Soltero"): 
        sueldoTotal = soltero
        print(f"El sueldo bruto de {nombreEmpleado} es de ${sueldoTotal}")
    else: 
        sueldoTotal = casado
        print(f"El sueldo bruto de {nombreEmpleado} es de ${sueldoTotal}")



