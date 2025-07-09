"""#verifica si el numero es positivo o negativo 
num1=float(input("ingrese un numero: "))
if num1 > 0:
    print(f"positivo porque es {num1}")
elif num1 < 0:
    print(f"es negativo porque ese {num1}")
else: 
    print(f"es cero{num1}")
 
 #calcula el mayor de dos numeros ingresados
nume1= float(input("ingrese un numero: "))
nume2= float(input("ingrese un numero: "))
if nume1>nume2:
    print(f"el numero {nume1} es mayor que {nume2}")
elif nume1<nume2:
    print(f"el numero {nume2} es mayor que {nume1}")
else:
    print(f"los numeros son iguales")

#determina si un numero es par o impar
numer1= int(input("ingrese un numero: "))
if numer1 % 2==0:
    print(f"el numero {numer1} es par ")
elif numer1 % 2==1:
    print (f"el numero {numer1} es impar")
else:
    print (f"el numero no es valido")

#dado un numero verifica si esta entre el 10 y el 20
nu1= int(input("ingrese un numero: "))
if nu1 < 10:
     print(f"el numero {nu1} es menor q 10 ")
elif nu1 > 20:
     print(f"el numero {nu1} es mayor q 20")
else:
     print(f"esta en entre el 10 y 20")

#dados tres numeros encuentra el mayor usando condicionales
a=int(input("Escribe el primer número: "))
b=int(input("Escribe el segundo número: "))
c=int(input("Escribe el tercer número: "))
if a>=b and a>=c:
    print("El mayor es:",a)
elif b >= a and b >= c:
    print("El mayor es:",b)
elif not (c<a or c<b):  
    print("El mayor es:",c)"""
