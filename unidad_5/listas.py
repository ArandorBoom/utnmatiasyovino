#Actividad 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Actividad 2
cosas_que_me_gustan = ["chocolate", "música", "viajar", "leer", "programar"]
print("El penúltimo elemento es:", cosas_que_me_gustan[-2])

#Actividad 3
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("montaña")
lista_vacia.append("aventura")
print("Lista con palabras agregadas:", lista_vacia)

#Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista actualizada:", animales)

#Actividad 5
#1 - Crea una lista llamada numeros con cinco elementos: [8, 15, 3, 22, 7].
#2 - Busca el valor máximo con max(numeros), que en este caso es 22.
#3 Elimina ese valor máximo con remove(), por lo tanto, elimina el 22 de la lista.
#4 Imprime la lista actualizada, que ahora queda: [8, 15, 3, 7].

#Actividad 6
numeros = list(range(10, 31, 5))
print("Los dos primeros números son:", numeros[:2])

#Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"
autos[2] = "coupe"
print("Lista actualizada de autos:", autos)

#Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

#Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
compras[0].remove("pan")
print("Lista actualizada de compras:", compras)

#Actividad 10
lista_anidada = [
    15,                     # lista_anidada[0]
    True,                  # lista_anidada[1]
    [25.5, 57.9, 30.6],    # lista_anidada[2][0], [2][1], [2][2]
    False                  
]
print("Lista anidada:", lista_anidada)

