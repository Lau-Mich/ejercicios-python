# 1: Crear las listas vacías
LISTA1 = []
LISTA2 = []

# 2: Añadir a la LISTA1 el int 100 y luego el string "Hola Mundo"
LISTA1.append(100)
LISTA1.append("Hola Mundo")

# 3: Añadir a la LISTA2 el string "Hola y Adiós" y luego el int 300
LISTA2.append("Hola y Adiós")
LISTA2.append(300)

# 4: Generar LISTA3 con todos los elementos de LISTA1 sin el último elemento
LISTA3 = LISTA1[:-1]

# 5: Generar LISTA4 con todos los elementos de LISTA2 menos el primero y el último
LISTA4 = LISTA2[1:-1]

# 6: Generar LISTA5 con los elementos de LISTA4 y LISTA3
LISTA5 = LISTA4 + LISTA3

# Imprimir resultados (opcional para ver los resultados)
print("LISTA1:", LISTA1)
print("LISTA2:", LISTA2)
print("LISTA3:", LISTA3)
print("LISTA4:", LISTA4)
print("LISTA5:", LISTA5)