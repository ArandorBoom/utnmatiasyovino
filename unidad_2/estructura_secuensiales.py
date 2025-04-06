import math

# Actividad 1 
print("Hola Mundo!")

# Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Actividad 4
radio = float(input("Ingrese radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area es {area:.2f} y el perimetro es {perimetro:.2f} ")

# Actividad 5
segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"Cantidad de horas {horas:.2f}")

# Actividad 6
numero = int(input("Ingrese el numero: "))
for i in range(1, 11):
    print(f"{numero} * {i} = {numero*i}")

# Actividad 7
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
print(f"El valor de la suma es: {numero1+numero2}")
print(f"El valor de la division de los numeros es: {numero1/numero2}")
print(f"El valor de la multiplicacion de los numeros es: {numero1*numero2}")
print(f"El valor de la resta de los numeros es: {numero1-numero2} ")

# Actividad 8
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura ** 2)
print(f"Su imc es : {imc:.2f}")

# Actividad 9
temperaturaCelsius = float(input("Ingrese temperatura en grados Celsius: "))
tempFahrenheit = (9 / 5) * temperaturaCelsius + 32
print(f"El valor de la temperatura en Fereheint es: {tempFahrenheit:.2f}")

#Actividad 10
numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))
numero3 = float(input("Ingrese tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El valor promedio es: {promedio:.2f}")