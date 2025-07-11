"""#1. determinar edad 
edad=int(input("ingresa tu edad: "))
if edad<18:
    print(f"usted es menor de edad")
elif edad>=65:
    print(f"usted es adulto mayor")
else:
    print(f"usted es mayor de edad")

#2. estatura 
estatura=float(input("ingresa tu estatuta en metros:"))
if estatura<1.5:
    print(f"usted es de estatura baja")
elif estatura>=1.5 ==1.8:
    print(f"usted es de estatura media")
else:
    print(f"usted es alto")

#3. multipo de 2 y 3
multlipo=int(input("ingrese un numero: "))
if multlipo % 2 == 0:
    print(f"este numero es multlipo del 2")
elif multlipo % 3 == 0:
    print(f"este numero es multlipo del 3")
else:
    print(f"no es multlipo de ninguno de los dos")

#4. Decimales
numero=input("Ingresa un número decimal: ")
partes=numero.split(".")
if len(partes) == 2 and len(partes[1])<= 2:
    print("Tiene 1 o 2 decimales.")
else:
    print("Tiene más de 2 decimales.")

#5. Pais en tupla
pais=input("ingresa un Pais: ")
paises= ("colombia", "peru", "argentina", "mexico")
if pais in paises:
    print(f"si esta en la tupla")
else:
    print(f"no esta en la tupla")

#6. tipo de sangre
tipo = input("Ingresa tu tipo de sangre (A, B, AB, O): ").upper()
compatibilidad = {
    "A": "Puede recibir de A y O",
    "B": "Puede recibir de B y O",
    "AB": "Puede recibir de todos",
    "O": "Solo puede recibir de O"
}
if tipo in compatibilidad:
    print("Compatibilidad:", compatibilidad[tipo])
else:
    print("Tipo de sangre no válido.")"""

#7. temperatura en Cº
temperatura=float(input("ingresar temperatura: "))
if temperatura <10:
    print(f"Hace frio")
elif temperatura >=10 ==25:
    print(f"templado")
else:
    print(f"Hace calor")

#8. menu con opciones 
