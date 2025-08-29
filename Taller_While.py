"""#EJERCICIO 1= Suma hasta cero
print("------ejercicio 1------")

totaly=0
while True:
    num = int(input("Ingresa un número entero (0 para terminar): "))
    if num == 0:
        break
    else:
       totaly = totaly + num
print("La suma total es:",totaly)
print("finalizo el bucle")

#EJERCICIO 2= Contraseña secreta
print("------ejercicio 2------")

contraseña= ""
while contraseña!= "python123":
     contraseña = input("Ingresa una contraseña: ") 
print("Contraseña correcta, has ingresado")

#EJERCICIO 3= Lista de compras
print("------ejercicio 3------")

producto = ""
lista = ""  

while producto != "fin":
    producto = input("Escribe un producto ('fin' para terminar): ")
    if producto != "fin":
        lista = lista + "- " + producto + "\n"  #use salto de linea para para que cada producto quede en una linea distinta

print("\nLista de compras:")
print(lista)

#EJERCICIO 4= Contador de pares e impares
print("------ejercicio 4------")

contador = 0
pares = 0
impares = 0

while contador < 10:
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    contador = contador + 1
print("Números pares:", pares)
print("Números impares:",impares)

#EJERCICIO 5= Promedio de calificaciones
print("------ejercicio 5------")

notas = []
suma = 0
contador = 0

while True:
    entrada = input("Ingresa una nota (o escribe salir): ")
    
    if entrada == "salir":
        break
    
    nota = float(entrada)
    notas.append(nota)
    suma = suma + nota
    contador = contador + 1

if contador > 0:
    promedio = suma / contador
    print("Notas:", notas)
    print("Promedio:", promedio)
else:
    print("No se ingresaron notas.")

#EJERCICIO 6= Tabla de multiplicar interactiva
print("------ejercicio 6------") 

numero = int(input("Ingresa un número: "))
multiplicador = 1

while multiplicador <= 10:
    print(numero, "x", multiplicador, "=", numero * multiplicador)
    multiplicador = multiplicador+1

#EJERCICIO 7= Adivina el numero
print("------ejercicio 7------") 

secreto = 17
numero = int(input("Adivina el número secreto: "))

while numero != secreto:
    if numero < secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")
    numero = int(input("Intenta de nuevo: "))

print("Correcto! El número secreto era",secreto)

#EJERCICIO 8= Tupla de frutas
print("------ejercicio 8------") 

frutas = ("maracuya", "mondongo", "kiwi", "zapallo")
respuesta = input("Adivina una fruta: ")

while respuesta != "mondongo":
    print("Esa fruta no es, intenta otra...")
    respuesta = input("Adivina una fruta: ")
print("Muy bien! Adivinaste:", respuesta)

#EJERCICIO 9= Diccionario de traduccion
print("------ejercicio 9------") 

# Diccionario con palabras
diccionario = {
    "gato": "cat",
    "perro": "dog",
    "casa": "house",
    "libro": "book",
    "agua": "water"
}


palabra = input("Escribe una palabra en español (o salir): ")

while palabra != "salir":
    print(diccionario.get(palabra, "No está en el diccionario"))
    palabra = input("Escribe otra palabra en español (o salir): ")

print("Programa terminado")

#EJERCICIO 10= Calculadora basica
print("------ejercicio 10------") 

opcion=[]

while opcion != 5:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a + b)

    if opcion == 2:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a - b)

    if opcion == 3:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a * b)

    if opcion == 4:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a / b)

print("Programa terminado")

#EJERCICIO 11= Registro de edades
print("------ejercicio 11------") 
personas = {}

while True:
    nombre = input("Ingresa un nombre (o escribe salir): ")

    if nombre == "salir":
        break

    edad = int(input("Ingresa la edad: "))
    personas[nombre] = edad  

print("Personas registradas:", personas)

#EJERCICIO 12= Buscar en lidta
print("------ejercicio 12------") 

colores = ["rojo", "azul", "verde", "amarillo", "negro"]
encontrado = False 

while encontrado == False:
    color = input("Escribe un color: ")

    if color == "rojo":
        encontrado = True
    elif color == "azul":
        encontrado = True
    elif color == "verde":
        encontrado = True
    elif color == "amarillo":
        encontrado = True
    elif color == "negro":
        encontrado = True
    else:
        print("Ese color no está, intenta de nuevo...")

print("Bien! Encontraste un color de la lista:", color)

#EJERCICIO 13= Potencias de un numero
print("------ejercicio 13------") 

num = int(input("Escribe un número: "))
i = 1

while i <= 5:
    print(num, "elevado a", i, "=", num ** i)
    i=i+1


#EJERCICIO 14= lista de cuadrados
print("------ejercicio 14------") 

lista = [] 
i = 0 
while True:
    numero = int(input("Ingresa un numero: "))
    cuadrado = numero **2 
    print(f"{numero} ** 2 = {cuadrado}")  
    lista.append(cuadrado) 
    i += 1
    if i == 5: 
        break 

print(f"Lista de los cuadrados  = {lista}")

#EJERCICIO 15= Diccionario de estudiantes
print("------ejercicio 15------") 

estudiantes = {}

while True:
    nombre = input("Escribe el nombre del estudiante (o salir): ")
    if nombre == "salir":
        break
    nota = float(input("Escribe la nota: "))
    estudiantes[nombre] = nota

print("Estudiantes registrados:", estudiantes)"""
