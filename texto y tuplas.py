texto= """Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. ..

La posición de Washington hacia las elecciones en Palestina ha sido coherente. Las elecciones fueron postergadas hasta la muerte de Yasser Arafat, que fue recibida como una oportunidad para la realización de la "visión" de Bush sobre un eventual Estado palestino democrativo, que es una palido y vago reflejo del consenso internacional sobre una acuerdo de dos entidades estatales en la zona, que Estados Unidos viene bloqueando desde hace 30 años....

El compromiso formal de Hamas de "destruir Israel" lo pone a la par con Estados Unidos e Israel, que prometieron por mucho tiempo que no habria ningun "Estado palestino adicional" (aparte de Jordania", hasta que ambas naciones aflojaron parcialmente su posicion, para aceptar un mini Estado constituido por los fragmentos que queden despues que Israel se apropie de todas las partes de Palestina que desea....

Simplemente como conjetura, imagine el lector una inversion de las circunstancias: que Hamas permitiese a los israelies vivir en cantones desparramados e invariables, virtualmente separados unos de otros, y en alguna pequeña parte de Jerusalen, mientras los palestinos construyen enormes asentamientos y proyectos de infraestructura para apoderarse de las tierras y los recursos de Israel, Y que, ademas Hamas acepte llamar a esos fragmentos "un Estado". Si se hicieran propuestas para esta empobrecida "categoria de Estado", nosotros nos sentiriamos, con razon, horrorizados. Pero con ese tipo de propuestas, la posicion de Hamas seria esencialmente igual a la de Estados Unidos e Israel
buscar= texto.find("empobrecida")
extraer= texto
print(extraer)"""


"""mi_tupla= (1,2,3)
mi_lista= list(mi_tupla)
print(mi_lista)

mi_lista=[4,5,6]
mi_tupla= tuple(mi_lista)
print(mi_tupla)

#ejersicio 1
frutas=("manzana", "pera")
lista_frutas= list(frutas)
fruta1= input("ingresa una fruta: ")
lista_frutas.append(fruta1)
frutas_final= tuple(lista_frutas)
print(frutas_final)

#ejersicio 2
notas = (4.2, 3.8)
lista_notas = list(notas)
nueva_nota = float(input("Ingresa una nueva nota: "))
lista_notas.append(nueva_nota)
notas_final = tuple(lista_notas)
print("Tupla final de calificaciones:", notas_final)

#ejersicio 3
persona = ("Ana", "Gómez")
lista_persona = list(persona)
documento = input("Ingresa el número de documento: ")
lista_persona.append(documento)
persona_final = tuple(lista_persona)
print("Tupla final con los datos personales:", persona_final)"""


"""#ejercicios practicos...
#tupla con los numeros del 1 al 5                                    '
tupla = (1, 2, 3, 4, 5)
# mostrar segundo valor 
print(tupla[1])
# cuantos elemento hay
print(len(tupla))
# encontrar posicion
print(tupla.index(4))
# crear una tupla q contenga otra tupla
tupla_externa=(1,2,(10,20,30),2)
# acceder al primr valor de mi tupla interna
primer_valor_interno=tupla_externa[2][0]
# mostrar el resultado
print(f"el valor de la tupla interna es:{primer_valor_interno}")"""




