# 1. registrar 3 frutas
frutas = []
print(frutas)
fruta = input("ingresa la primera fruta: ")
frutas.append(fruta)
fruta2 = input("ingresa la segunda fruta: ")
frutas.append(fruta2)
fruta3 = input("ingresa la tercera fruta: ")
frutas.append(fruta3)
print(frutas)

# 2. guardar 2 edades
edades = []
print(edades)
e1 = input("ingresa tu edad: ")
edades.append(e1)
e2 = input("ingresa tu edad: ")
edades.append(e2)
print(edades)

# 3. notas de 2 estudiantes
notas = []
print(notas)
nota1 = input("ingrese una nota: ")
notas.append(nota1)
nota2 = input("ingresa una nota: ")
notas.append(nota2)
print(notas)

# 4. productos en una bolsa
productos = []
print(productos)
pro1 = input("ingrese el nombre de un producto: ")
productos.append(pro1)
pro2 = input("ingrese el nombre de un producto: ")
productos.append(pro2)
pro3 = input("ingrese el nombre de un producto: ")
productos.append(pro3)
print(productos)

# 5. precios de 3 articulos
precios = []
print(precios)
precio1 = float(input("ingresa un precio: "))
precios.append(precio1)
precio2 = float(input("ingrese un precio: "))
precios.append(precio2)
precio3 = float(input("ingrese un precio: "))
precios.append(precio3)
print(precios)
total = precio1 + precio2 + precio3
print("la suma total es:", total)

# 6. numeros ingresados por el usuario
numeros = []
print(numeros)
no1 =input("ingrese un numero: ")
numeros.append(no1)
no2 = input("ingrese un numero: ")
numeros.append(no2)
no3 = input("ingrese un numero: ")
numeros.append(no3)
print(numeros)

#7. registrar dos nombres completos 
nombres = []
print(nombres)
nom1= input("ingrese un nombre: ")
nombres.append(nom1)
nom2= input("ingrese otro nombre: ")
nombres.append(nom2)
print(nombres)

#eliminacion en una lista
#ejersicio 
futbol=["cali","america","nacional","pasto","medellin"]
futbol.remove("cali")
print (futbol)

#ejersicio 1
#1
lista = []
lista.append(7)
print(lista) 
#2 
nombres = ["Ana", "Luis"]
nombres.append("Carlos")
print(nombres)  

#ejersicio 2
#1
numeros = [1, 2, 3]
numeros.insert(0, 99)
print(numeros)
#2 
colores = ["azul", "verde"]
colores.insert(1, "rojo")
print(colores)  

# ejercicio 3
# 1
lista3 = [1, 2, 3]
lista3.extend([4, 5, 6])
print(lista3)
# 2
letras = ["a", "b"]
letras.extend("ok")
print(letras)

# ejercicio 4
# 1
frutas = ["manzana", "uva", "pera"]
frutas.remove("uva")
print(frutas)
# 2
lista4 = [1, 2, 3, 2]
lista4.remove(2)
print(lista4)

# ejercicio 5
# 1
lista5 = [1, 2, 3, 4]
lista5.pop()
print(lista5)
# 2
lista6 = ["uno", "dos", "tres"]
lista6.pop(0)
print(lista6)

# ejercicio 6
# 1
lista7 = [1, 2, 3]
lista7.clear()
print(lista7)
# 2
lista8 = [1, 2, 3, 4, 5]
lista8.clear()
print(lista8)

# ejercicio 7
# 1
frutas1 = ["manzana", "pera", "uva"]
posicion = frutas1.index("pera")
print(posicion)
# 2
numeros = [4, 5, 6, 7]
indice = numeros.index(6)
print(indice)

# ejercicio 8
# 1
lista9 = [3, 1, 3, 5, 3]
veces1 = lista9.count(3)
print(veces1)
# 2
lista10 = ["a", "b", "a", "c", "a"]
veces2 = lista10.count("a")
print(veces1)

# ejercicio 9
# 1
lista11 = [5, 1, 4, 2, 3]
lista11.sort()
print(lista11)
# 2
lista12 = ["z", "a", "m", "b"]
lista12.sort()
print(lista12)

# ejercicio 10
# 1
lista13 = [1, 2, 3, 4]
lista13.reverse()
print(lista13)
# 2
lista14 = ["inicio", "medio", "fin"]
lista14.reverse()
print(lista14)

# ejercicio 11
# 1
lista_original1 = [1, 2, 3]
copia_lista1 = lista_original1.copy()
print(copia_lista1) 
# 2
lista_original2 =[ "a", "b", "c"]
copia_lista1 = lista_original2.copy()
copia_lista1.append("d")
print(lista_original2)
print(copia_lista1)