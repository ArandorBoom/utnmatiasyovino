# Práctico	4:	Estructuras	repetitivas	
import random

# Actividad 1
for i in range(101):
    print(i)

# Actividad 2
numero = int(input("Ingrese un numero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"La cantidad de digitos es: {cantidad_digitos}")

# Actidad 3
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
menor, mayor = min(numero, numero2), max(numero, numero2)
suma = sum(range(menor+1, mayor))
print(f"La suma de los numeros es: {suma}")

# Actividad 4
total = 0

while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")

# Actividad 5
numero_secreto = random.randint(0,9) 
intentos = 0 

while True:  
   numero = int(input("Ingrese un numero de 0 a 9 para adivinar el correcto: ")) 
   if numero_secreto == numero:
       print(f"Muy bien adivinaste el numero en {intentos} intentos")
       break
   else:
       print("Numero equivocado! intenta de nuevo")

# Actividad 6
for i in range(100 , -1 , -2):
    print(i)

# Actividad 7
while True:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:    
        print("El numero debe ser positivo")
        continue
    else:
        suma = sum(range(numero+1))
        print(f"La suma es: {suma}")
        break

# Actividad 8
cantidad = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de numeros positivos: {positivos}")


# Actividad 9
cantidad = 100
suma = 0

for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    suma += numero
media = suma/cantidad
print(f"El promedio de la suma de los numeros es: {media}")

# Actividad 10
numero = input("Ingrese un numero: ")
numero_invertido = numero[::-1]
print(f"El numero invertido es: {numero_invertido}")
