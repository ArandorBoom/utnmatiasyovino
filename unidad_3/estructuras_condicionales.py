# Práctico 3: Estructuras condicionales  

# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.") 

# Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
elif nota < 6:
    print("Desaprobado")

# Actividad 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Has ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

# Actividad 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es un niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a Joven")
else:
    print("Adulto/a")

# Actividad 5
contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Has ingresado una contraseña correcta.")
else:
    print("Por favor, Ingrese una contraseña entre 8 y 14 caracteres.")

# Actividad 6
import random
from statistics import mode, median, mean


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if media > mediana and mediana > moda:
    print("Sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("Sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("La distribución no encaja claramente en un sesgo definido.")

# Actividad 7
frase = input("Ingrese frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# Actividad 8
nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Mostrar el nombre en MAYUSCULAS")
print("2. Mostrar el nombre en minusculas")
print("3. Mostrar el nombre con la primera letra en mayuscula")
opcion = int(input("Ingrese 1, 2 o 3: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no valida. Por favor ingrese 1, 2 o 3.")

# Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))


if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# Actividad 10
hemisferio = input("¿En que hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingresa el numero del mes (1 a 12): "))
dia = int(input("Ingresa el día del mes (1 a 31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no valida"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no reconocido"
print(f"La estacion del año es: {estacion}")