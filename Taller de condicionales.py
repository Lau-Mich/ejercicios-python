#1 verifica si el numero es positivo o negativo 
num1=float(input("ingrese un numero: "))
if num1 > 0:
    print(f"positivo porque es {num1}")
elif num1 < 0:
    print(f"es negativo porque ese {num1}")
else: 
    print(f"es cero{num1}")
 
 #2 calcula el mayor de dos numeros ingresados
nume1= float(input("ingrese un numero: "))
nume2= float(input("ingrese un numero: "))
if nume1>nume2:
    print(f"el numero {nume1} es mayor que {nume2}")
elif nume1<nume2:
    print(f"el numero {nume2} es mayor que {nume1}")
else:
    print(f"los numeros son iguales")

#3 determina si un numero es par o impar
numer1= int(input("ingrese un numero: "))
if numer1 % 2==0:
    print(f"el numero {numer1} es par ")
elif numer1 % 2==1:
    print (f"el numero {numer1} es impar")
else:
    print (f"el numero no es valido")

#4 dado un numero verifica si esta entre el 10 y el 20
nu1= int(input("ingrese un numero: "))
if nu1 < 10:
     print(f"el numero {nu1} es menor q 10 ")
elif nu1 > 20:
     print(f"el numero {nu1} es mayor q 20")
else:
     print(f"esta en entre el 10 y 20")

#5 dados tres numeros encuentra el mayor usando condicionales
a=int(input("Escribe el primer número: "))
b=int(input("Escribe el segundo número: "))
c=int(input("Escribe el tercer número: "))
if a>=b and a>=c:
    print("El mayor es:",a)
elif b >= a and b >= c:
    print("El mayor es:",b)
elif not (c<a or c<b):  
    print("El mayor es:",c)

#6 calcula el precio final con un 10% de descuento si el total es mayor a 100
n1=float(input("Escribe el total de la compra: "))
if n1>100:
    descuento = n1 * 0.10
    precio_final = n1 - descuento   
    print("El precio final es:", precio_final)
elif n1== 100:
    print("El precio final es:", n1)
else:
    print("No tienes descuento.")
    print("El precio final es:", n1)

#7 Verifica si una persona puede votar (mayor o igual a 18 años).
edad = 20
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

#8 Descuento para tipo de cliente
tipo = "VIP"
precio = 100000
if tipo == "VIP":
    precio = precio * 0.8
print("Precio final:", precio)

#9 Verifica si un número es múltiplo de 5 y de 3 al mismo tiempo
numero = 15
if numero % 5 == 0 and numero % 3 == 0:
    print("Es múltiplo de 5 y de 3")
else:
    print("No es múltiplo de 5 y 3 al mismo tiempo")

#10 si un número es divisible entre dos números dados
num = 20
a = 5
b = 4
if num % a == 0 and num % b == 0:
    print(f"{num} es divisible entre {a} y {b}")
else:
    print(f"{num} NO es divisible entre {a} y {b}")

# 11 Tercer número mayor que 10
numeros = [3, 8, 15, 2, 7]
if numeros[2] > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")

# 12 Verifica si 7 está en la lista
mi_lista = [3, 5, 7, 9]
print("Está en la lista" if 7 in mi_lista else "No está en la lista")

# 13 Suma de los primeros 3
lista = [4, 6, 2, 8]
suma = sum(lista[:3])
if suma > 10:
    print("Suma alta")
else:
    print("Suma baja")

# 14 Verifica nombre en lista
nombres = ["Ana", "Luis", "Pedro", "Marta"]
if "Marta" in nombres:
    print("Nombre correcto")
else:
    print("Nombre diferente")

# 15 Cambiar segundo color si es azul
colores = ["rojo", "azul", "verde"]
if colores[1] == "azul":
    colores[1] = "amarillo"
print(colores)

#16 Verifica orden de tupla
t = (5, 8, 12, 20)
if t[0] < t[-1]:
    print("Orden ascendente")
else:
    print("Orden descendente")

#17 Edad mayor a 30
tupla = (25, 32, 28)
print("Edad mayor a 30" if tupla[1] > 30 else "Edad menor o igual a 30")

#18 Convertir tupla a lista y modificar
tup = (1, 2, 3)
lista = list(tup)
if lista[1] == 2:
    lista[1] = 10
tup = tuple(lista)
print(tup)

#19 Coordenada alta o baja
coordenada = (4, 9)
if coordenada[1] > 5:
    print("Coordenada alta")
else:
    print("Coordenada baja")

#20 Comparar tuplas
a = (3, 4)
b = (3, 5)
if a == b:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")

#21 Diccionario con edad
persona = {"nombre": "Juan", "edad": 17}
if persona["edad"] >= 18:
    print("Adulto")
else:
    print("Menor de edad")

#22 Cambiar valor si cumple condición
persona = {"nombre": "Lucía", "edad": 20}
if persona["edad"] > 18:
    persona["edad"] = 21
print(persona)

#23 revisar si tiene "edad"
persona = {"nombre": "Camilo", "edad": 19}
if "edad" in persona:
    print("Edad:", persona["edad"])
else:
    print("No tiene edad")

#24 si "activo" es falso, cambiarlo
usuario = {"nombre": "Laura", "activo": False}
if usuario.get("activo") == False:
    usuario["activo"] = True
print(usuario)

#25 revisar cuantas claves tiene
datos = {"nombre": "Sofía", "edad": 22, "ciudad": "Cali"}
if len(datos) > 2:
    print("Diccionario completo")
else:
    print("Diccionario incompleto")