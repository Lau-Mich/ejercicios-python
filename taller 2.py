#taller 2

#Calculadora de promedio
a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
c = float(input("Nota 3: "))
prom = (a + b + c) / 3
print("El promedio es:", prom)

#Actualiza precios
prod1 = input("Producto 1: ")
precio1 = float(input("Precio: "))
prod2 = input("Producto 2: ")
precio2 = float(input("Precio: "))
prod3 = input("Producto 3: ")
precio3 = float(input("Precio: "))
aumento = float(input("Aumento en %: "))
precio1 += precio1 * aumento / 100
precio2 += precio2 * aumento / 100
precio3 += precio3 * aumento / 100
print(prod1, "nuevo precio:", precio1)
print(prod2, "nuevo precio:", precio2)
print(prod3, "nuevo precio:", precio3)

#Conversor de temperaturas
t1 = int(input("Día 1: "))
t2 = int(input("Día 2: "))
t3 = int(input("Día 3: "))
t4 = int(input("Día 4: "))
t5 = int(input("Día 5: "))
f1 = (t1 * 9/5) + 32
f2 = (t2 * 9/5) + 32
f3 = (t3 * 9/5) + 32
f4 = (t4 * 9/5) + 32
f5 = (t5 * 9/5) + 32
print("Temperaturas en Fahrenheit:")
print(f1, f2, f3, f4, f5)

#Edad promedio
e1 = int(input("Edad 1: "))
e2 = int(input("Edad 2: "))
e3 = int(input("Edad 3: "))
e4 = int(input("Edad 4: "))
e5 = int(input("Edad 5: "))
mayor = max(e1, e2, e3, e4, e5)
menor = min(e1, e2, e3, e4, e5)
prom = (e1 + e2 + e3 + e4 + e5) / 5
print("Mayor:", mayor)
print("Menor:", menor)
print("Promedio:", prom)

#Frutas y precios
p_manzana = 3000
p_papaya = 1000
p_uva = 5000
k1 = float(input("Kilos manzana: "))
k2 = float(input("Kilos papaya: "))
k3 = float(input("Kilos uva: "))
total = (k1 * p_manzana) + (k2 * p_papaya) + (k3 * p_uva)
print("Total a pagar:", total)

#Suma tupla
numeros = (5, 8, 2, 10, 7)
suma_total = sum(numeros)
print("La suma total es:", suma_total)

#Inventario
nombre1 = input("Nombre del producto 1: ")
cantidad1 = int(input("Cantidad del producto 1: "))
precio1 = float(input("Precio por unidad del producto 1: "))
nombre2 = input("Nombre del producto 2: ")
cantidad2 = int(input("Cantidad del producto 2: "))
precio2 = float(input("Precio por unidad del producto 2: "))
nombre3 = input("Nombre del producto 3: ")
cantidad3 = int(input("Cantidad del producto 3: "))
precio3 = float(input("Precio por unidad del producto 3: "))

total1 = cantidad1 * precio1
total2 = cantidad2 * precio2
total3 = cantidad3 * precio3
total_general = total1 + total2 + total3
print("Total del inventario es:", total_general)

# Descuento
desc1 = float(input("ingresa el descuento q quieres: "))
desc2 = float(input("ingresa otro: "))
desc3= float(input("otro mas: "))
desc4= float(input("uno de mas: "))
desc5 = float(input("el ultimo: "))
descuento = float(input("Descuento %: "))
desc1 -= desc1 * descuento/ 100
desc2 -= desc2* descuento/ 100
desc3 -= desc3* descuento/ 100
desc4 -= desc4* descuento/ 100
desc5 -= desc5 * descuento/ 100
print("Precios nuevos:", desc1,desc2,desc3,desc4,desc5)

#Notas con tupla
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

mayor = nota1
menor = nota1
if nota2 > mayor:
    mayor = nota2
if nota3 > mayor:
    mayor = nota3
if nota4 > mayor:
    mayor = nota4

if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3
if nota4 < menor:
    menor = nota4

print("Nota más alta:", mayor)
print("Nota más baja:", menor)

#Conversión
unidad = input("Unidad (km, m, cm): ")
valor = float(input("Cantidad: "))
if unidad == "km":
    metros = valor * 1000
elif unidad == "cm":
    metros = valor * 0.01
else:
    metros = valor
print("Resultado en m:", metros)

#IVA
precio1 = float(input("Precio 1: "))
precio2 = float(input("Precio 2: "))
precio3 = float(input("Precio 3: "))
precio4 = float(input("Precio 4: "))
precio5 = float(input("Precio 5: "))
precio1 = precio1 * 1.19
precio2 = precio2 * 1.19
precio3 = precio3 * 1.19
precio4 = precio4 * 1.19
precio5 = precio5 * 1.19
print("Precios con IVA:", precio1, precio2, precio3, precio4, precio5)

#Operaciones con tupla
x = int(input("Número 1: "))
y = int(input("Número 2: "))
suma = x + y
resta = x - y
multi = x * y
if y != 0:
    div = x / y
else:
    div = "No se puede dividir por 0"
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multi)
print("División:", div)

#Diccionario estudiantes
nombre1 = input("Nombre del estudiante 1: ")
nota1 = float(input("Nota del estudiante 1: "))
nombre2 = input("Nombre del estudiante 2: ")
nota2 = float(input("Nota del estudiante 2: "))
nombre3 = input("Nombre del estudiante 3: ")
nota3 = float(input("Nota del estudiante 3: "))
suma_notas = nota1 + nota2 + nota3
promedio = suma_notas / 3
print("El promedio general es:", promedio)

#Salarios
sal1 = float(input("Salario 1: "))
sal2 = float(input("Salario 2: "))
sal3 = float(input("Salario 3: "))
sal4 = float(input("Salario 4: "))
sal5 = float(input("Salario 5: "))
sal1 += sal1 * 0.10
sal2 += sal2 * 0.10
sal3 += sal3 * 0.10
sal4 += sal4 * 0.10
sal5 += sal5 * 0.10
print("Salarios nuevos:", sal1, sal2, sal3, sal4, sal5)

#Impuestos
producto1 = input("Producto 1: ")
precio1 = float(input("Precio: "))
producto2 = input("Producto 2: ")
precio2 = float(input("Precio: "))
producto3 = input("Producto 3: ")
precio3 = float(input("Precio: "))
imp = float(input("Impuesto %: "))
print(producto1, "con impuesto:", precio1 + precio1 * imp / 100)
print(producto2, "con impuesto:", precio2 + precio2 * imp / 100)
print(producto3, "con impuesto:", precio3 + precio3 * imp / 100)

#Edad análisis
edad1 = int(input("Edad 1: "))
edad2 = int(input("Edad 2: "))
edad3 = int(input("Edad 3: "))
edad4 = int(input("Edad 4: "))
edad5 = int(input("Edad 5: "))

mayores = 0
menores = 0

if edad1 >= 18:
    mayores = mayores + 1
else:
    menores = menores + 1

if edad2 >= 18:
    mayores = mayores + 1
else:
    menores = menores + 1

if edad3 >= 18:
    mayores = mayores + 1
else:
    menores = menores + 1

if edad4 >= 18:
    mayores = mayores + 1
else:
    menores = menores + 1

if edad5 >= 18:
    mayores = mayores + 1
else:
    menores = menores + 1

print("Cantidad de mayores de edad:", mayores)
print("Cantidad de menores de edad:", menores)

#Conversión moneda
d = float(input("Dólares: "))
euros = d * 1.1
pesos = d * 4000
yenes = d * 150
print("Euros:", euros)
print("Pesos:", pesos)
print("Yenes:", yenes)

#Ventas
producto1 = input("Nombre del producto 1: ")
cantidad1 = int(input("Cantidad vendida del producto 1: "))
producto2 = input("Nombre del producto 2: ")
cantidad2 = int(input("Cantidad vendida del producto 2: "))
producto3 = input("Nombre del producto 3: ")
cantidad3 = int(input("Cantidad vendida del producto 3: "))
total_vendido = cantidad1 + cantidad2 + cantidad3
print("Total de unidades vendidas:", total_vendido)

#Temperaturas extremas
precio1 = int(input("Precio 1: "))
precio2 = int(input("Precio 2: "))
precio3 = int(input("Precio 3: "))
precio4 = int(input("Precio 4: "))
precio5 = int(input("Precio 5: "))

# Lista original
list1=int(input())
list2=int(input())
list3=int(input())
list4=int(input())
list5=int(input())
lis6=int(input())
list7=int(input())
list8=int(input())
list9=int(input())
lis10=int(input())

altas = 0
bajas = 0
for x in [list1,list2,list3,list4,list5,lis6,list7,list8,list9,lis10]:
    if x > 30: altas += 1
    if x < 10: bajas += 1

print(altas)
print(bajas)

#Lista de precios
precios = [precio1, precio2, precio3, precio4, precio5]
precio_eliminar = int(input("¿Qué precio quieres eliminar?: "))
if precio_eliminar in precios:
    precios.remove(precio_eliminar)

precio_nuevo = int(input("Nuevo precio a agregar: "))
precios.append(precio_nuevo)
precio_insertar = int(input("Otro precio para insertar en posición 1: "))
precios.insert(1, precio_insertar)
precios.sort()
print("Lista de precios final:", precios)
           