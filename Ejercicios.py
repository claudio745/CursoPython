# Ejercicio 1
# Escribir un programa que pregunte el nombre al usuario y un numero entero. Imprima por consola el nombre del usuario, uno por linea,
# tantas veces como el numero introducido

nombre_usuario = input("Indique su nombre: ")
num = int(input("Ingrese un numero entero: "))

contador = 0

while contador < num:
    print(nombre_usuario)
    contador +=1

# Ejercicio 2
# Escribir por pantalla el resultado de la siguiente operacion aritmetica: 

operacion_aritmetica = (((3+2)/(2*5))**2)

print("El resultado de la operacion es: " +str(operacion_aritmetica))

# Ejercicio 3
# Una jugueteria tiene mucho exito en 2 de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logistica
# cobra por peso de cada paquete, asi que deben calcular el peso de los payasos y muñecas que saldrian en cada paquete a demanda
# Cada payaso pesa 112g y cada muñeca 75g. Escribir un codigo que lea el numero de payasos y muñecas vendidos en el ultimo pedido 
# y calcule el peso total del paquete que sera enviado.


payasos = int(input("Ingrese el número de payasos vendidos: "))
muñecas = int(input("Ingrese número de muñecas vendidas: "))

peso_payasos = 112
peso_muñecas = 75

peso_total = (payasos * peso_payasos) + (muñecas * peso_muñecas)

print("El peso total del pedido es: " +str(peso_total) + " gramos")

# Ejercicio 4
