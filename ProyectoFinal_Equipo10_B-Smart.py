"""
Proyecto Final Pensamineto Computacional
Equipo 10
Karen Michelle López Guajardo
Andrea Yamileth Florencia Ortiz
David Martínez Celis González
"""
"""
Casos de prueba
%Run ProyectoFinal_Equipo10_B-Smart.py
¡Hola, bienvenido/a a la plataforma B-Smart!
Aquí podrás estudiar para tu examen PISA en las áreas de Matemáticas y Química
A continuación te presentamos los temas que podrás práticar en el programa

1- La Tabla Periódica y Balancear Ecuaciones Químicas
2- Teorema de Pitágoras
3- Tendencias de Medida Central
4- Despejar x de Ecuaciones
5- Razones/Ratios

Por favor escribe tu nombre: David
Por favor escribe el número del tema que te gustaría prácticar hoy: 5
David escogiste Razones/Ratios, ¡mucha suerte!

Hola David
Necesito tu ayuda. He encontrado una caja con un tesoro, pero no la puedo abrir ya que tiene una contraseña, que solo tú me puedes ayudar a encontrar. Para hacerlo, deberás responder a las siguientes preguntas, y si las sacas bien vas a obtener una pista que te va a ayudar a poder averiguar cada letra de la contraseña. ¡Tú puedes!

Pregunta 1
 En un salón de clases hay 16 mujeres y 14 hombres. 
 ¿Cuál es la razón de hombres contra mujeres?
a) 14/30 // b) 14/16 // c) 14/6 
Escribe la letra aquí: b
¡Respuesta correcta! Pista: Decima letra del abecedario
Dame primera letra de la contraseña del tesoro: J

Pregunta 2
 En una fiesta asistieron 22 jóvenes y 30 adultos. ¿Cuál es la razón de adultos contra el total?
a) 22/52 // b) 22/30 // c) 30/52 
Escribe la letra aquí: c
¡Respuesta correcta! Pista: Primer letra del país donde viven los kanguros
Dame segunda letra de la contraseña del tesoro: a

Pregunta 3
 Una tienda vende zapatos, donde la razón de pares de zapatos blancos a negros es de 1/4.
Si hay 15 pares de zapatos blancos, cuántos pares de zapatos negros hay en la tienda?
a) 45 // b) 60 // c) 15 
Escribe la letra aquí: a
¡Respuesta correcta! Pista: Primera letra de la capital de Francia
Dame tercera letra de la contraseña del tesoro:  P 

Pregunta 4
 La razón de estudiantes locales a estudiantes foráneos en un aula es de 5/8. Si hay 78 personas, cuántos estudiantes locales hay?
a) 30 // b) 24 // c) 50 
Escribe la letra aquí: b
Respueta equivocada, tendrás que adivinar primera letra sin pista :(
Dame segunda letra de la contraseña del tesoro: o

Pregunta 5
 La razón de un nieto y su abuelo es de 2 a 7. Las edades de ambos suman 63. Encuentra la edad del nieto.
a\) 49 // b\) 22 // c\) 14 
Escribe la letra aquí: c
¡Respuesta correcta! Pista: Letra número 14 en el abecedario
Dame segunda letra de la contraseña del tesoro: N

Felicidades, lograste abrir el tesoro
Tu contraseña fue japon
"""
import random as nd
#Se imprimen instrucciones para usuario, se presentarán temas y el debe escribir el número del tema que quiere practicar
print("¡Hola, bienvenido/a a la plataforma B-Smart!\nAquí podrás estudiar para tu examen PISA en las áreas de Matemáticas y Química")
print("A continuación te presentamos los temas que podrás práticar en el programa\n")
print("1- La Tabla Periódica y Balancear Ecuaciones Químicas\n2- Teorema de Pitágoras\n3- Tendencias de Medida Central")
print("4- Despejar x de Ecuaciones\n5- Razones/Ratios\n")

nombre = input("Por favor escribe tu nombre: ")
tema = input("Por favor escribe el número del tema que te gustaría prácticar hoy: ")

#sanity check
def esnumero(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

if esnumero(tema) == True:
    tema = int(tema)
    if tema < 1 or tema > 5:
        print("Dato invalido, por favor escribe solámente el número del tema que quieras prácticar")
        exit()
else:
    print("Dato invalido, por favor escribe solámente el número del tema que quieras prácticar")
    exit()

if tema == 1:
    print(nombre + " escogiste La Tabla Periódica y Balancear Ecuaciones Químicas, ¡mucha suerte!\n")
    print("Quizz de Quimica.")
    question1 =("\033[;31m"+"¿Cual es el número atómico del bromo?")
    options1 = "a. 30\nb. 25\nc. 35\nd. 34\n"
    print(question1)
    print(options1)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "c":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "c":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
    question2 = "\033[;33m"+"¿Cual es el peso atómico del nitrógeno?"
    options2 = "a. 10\nb. 14\nc. 13\nd. 9\n"
    print(question2)
    print(options2)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "b":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "b":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
    question3 ="\033[;32m"+"¿Cual es el número de protones en el sodio?"
    options3 = "a. 10\nb. 11\nc. 22\nd. 12\n"
    print(question3)
    print(options3)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "b":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "b":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
    question4 ="\033[;34m"+"¿Cuales son las siglas del selenio?"
    options4 = "a. S\nb. Se\nc. SE\nd. Ce\n"
    print(question4)
    print(options4)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "b":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "b":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
    question5 ="\033[;35m"+"¿El criptón a qué grupo pertenece?"
    options5 = "a. No metal\nb. Metaloide\nc. Gas Noble\nd. Alcanos\n"
    print(question5)
    print(options5)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "c":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "c":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
            
    question6 ="\033[;35m"+"Balance la siguiente equacion.\n _NaBr+_Cr2 →  _NaCl+ _ Br2"
    options6 = "a. 2NaBr+1Cr2 →  2NaCl+ 1Br2\nb. 2NaBr+2Cr2 →  1NaCl+ 1 Br2\nc.1NaBr+ 2Cr2 →  1NaCl+ 2Br2\nd. 3NaBr+2Cr2 →  1NaCl+ 3Br2\n"
    print(question6)
    print(options6)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "a":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "a":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
            
    question7 ="\033[;34m""Balance la siguiente equacion.\n__Mg+ _O2 → _MgO"
    options7 = "a. 2Mg+ 1O2 → 2MgO\nb. 3Mg+ 1O2 → 3MgO\nc.1Mg+ 2O2 → 2MgO\nd. 5Mg+ 2O2 → 5MgO\n"
    print(question7)
    print(options7)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "a":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "a":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break

    question8 ="\033[;36m"+"Balance la siguiente equacion.\n_H2+ _O2 → _H2O"
    options8 = "a. 2H2+ 1O2 → 2H2O\nb. 3H2+ 1O2 → 2H2O\nc.4H2+ 1O2 → 6H2O\nd. 5H2+ 1O2 → 5H2O\n"
    print(question8)
    print(options8)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "a":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "a":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
            
    question9 ="\033[;32m"+"Balance la siguiente equacion.\n_SiO2+ _HF → _SiF4 + _H2O"
    options9 = "a. 1SiO2+ 4HF → 1SiF4 + 2H2O\nb. 2SiO2+ 4HF → 1SiF4 + 2H2O\nc.1SiO2+ 4HF → 2SiF4 + 6H2O\nd. 1SiO2+ 3HF → 1SiF4 + 2H2O\n"
    print(question9)
    print(options9)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "a":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "a":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break
            
    question10 ="\033[;31m"+"Balance la siguiente equacion.\n_Cr2O3+ _Mg → _Cr+ _MgO"
    options10 = "a. 1Cr2O3+ 1Mg → 1Cr+ 1MgO\nb. 1Cr2O3+ 4Mg → 3Cr+ 6MgO\nc. 2Cr2O3+ 3Mg → 2Cr+ 3MgO\nd. 1Cr2O3+ 3Mg → 2Cr+ 3MgO\n"
    print(question10)
    print(options10)

    while True:
        response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

        if response == "d":
            print("Correcto")
            break
        else:
            print("Incorrecto!!! Vuelve intentar.")

            while True:
                response = input("Teclea 'a', 'b', 'c' o 'd' para tu respuesta\n")

                if response == "d":
                    print("Correcto")
                    stop = True
                    break
                else:
                    print("Incorrecto!!! Ya no cuentas con intentos.")
                    stop = True
                    break
            if stop:
                break

    
elif tema == 2:
    print(nombre + " escogiste Teorema de Pitágoras, ¡mucha suerte!\n")
    def preguntasm2():
        print("A continuación se mostrarán preguntas del tema de Teorema de pitágoras")
    #Se crea una lista para ir guardando las preguntas que se vayan generan de manera random   
        lista=[]
    #Se repitirá este numero de veces para que la probabilidad de que salgan todas las preguntas sea mayor
        for i in range(0,21):
    #Se genera el numero de pregunta de manera aleatoria randint
            pregunta = nd.randint(1,5)
    #Condicion para que mostrar las preguntas, siempre y cuando el numero de pregunta no se repita en la lista
            if pregunta in lista:
                pass
    #si la pregunta ya está en la lista se regresará al ciclo sin pasar a los otros condicionales
            elif pregunta == 1:
                print("P1.Dadas las siguientes medidas resuelve lo que se te pide. Ca=4 y Co=8, calcule la hipotenusa(Redondeo a 2 decimales)")
                print("8.94\n 8\n 9.15\n 7.82")
    #se registra la respuesta     
                resp1 = float(input("Introduzca la respuesta correcta: "))
    #se agrega el numero de pregunta a la lista            
                lista.insert(0,pregunta)
            elif pregunta == 2:
                print("P2.Dadas las siguientes medidas resuelve lo que se te pide. Ca=10 y Co=15, calcule la hipotenusa(Redondeo a 2 decimales).")
                print("14.05\n 10.12\n 18.02\n 17.09")
                resp2 = float(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 3:
                print("P3.Dadas las siguientes medidas resuelve lo que se te pide. Hip=7.5 y Co=9, calcule el cateto adyacente (Redondeo a 2 decimales).")
                print("3.12\n 4.97\n 5.62\n 6.42")
                resp3 = float(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 4:
                print("P4.Dadas las siguientes medidas resuelve lo que se te pide. Ca=9 y Co=6.5, calcule la hipotenusa(Redondeo a 2 decimales).")
                print("9.62\n 11.10\n 8.5\n 10.50")
                resp4 = float(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 5:
                print("P5.Dadas las siguientes medidas resuelve lo que se te pide. Ca=20 y Co=22.5, calcule la hipotenusa(Redondeo a 2 decimales).")
                print("38\n 25.61\n 30.10\n 15.42")
                resp5 = float(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            else:
                pass
    #se le llama a otra función para mostrar la califiación
        calificacionm2(resp1, resp2, resp3, resp4, resp5)

    def calificacionm2(resp1, resp2, resp3, resp4, resp5):
    #se usarán condicionales para evaluar las respuestas que se recibieron    
        if resp1 == 8.94:
            x1 = 1
            print("P1: Respuesta correcta ☻")
        else:
            x1 = 0
            print("P1: UPPS... Respuesta incorrecta :c")
        if resp2 == 18.02:
            x2 = 1
            print("P2: Respuesta correcta ☻")
        else:
            x2 = 0
            print("P2: UPPS... Respuesta incorrecta :c")
        if resp3 == 4.97:
            x3 = 1
            print("P3: Respuesta correcta ☻")
        else:
            x3 = 0
            print("P3: UPPS... Respuesta incorrecta :c")
        if resp4 == 11.10:
            x4 = 1
            print("P4: Respuesta correcta ☻")
        else:
            x4 = 0
            print("P4: UPPS... Respuesta incorrecta :c")
        if resp5 == 30.10:
            x5 = 1
            print("P5: Respuesta correcta ☻")
        else:
            x5 = 0
            print("P5: UPPS... Respuesta incorrecta :c")
    #se hae un promedio de lo que se obtuvo para después mostrar la calificación en terminos de 0/100
        calificacion = ((x1 + x2 + x3 + x4 + x5)/5)*100 
        print("Su calificación fue de: ", calificacion)
    #se ejecuta la función en el código general
    preguntasm2()
    
    
elif tema == 3:
    print(nombre + " escogiste Tendencias de Medida Central, ¡mucha suerte!\n")
    def preguntasm():
        print("A continuación se mostrarán preguntas del tema de Tendencias de medida central")
    #Se crea una lista para ir guardando las preguntas que se vayan generan de manera random
        lista=[]
    #Se repitirá este numero de veces para que la probabilidad de que salgan todas las preguntas sea mayor
        for i in range(0,21):
    #Se genera el numero de pregunta de manera aleatoria randint
            pregunta = nd.randint(1,5)
    #Condicion para que mostrar las preguntas, siempre y cuando el numero de pregunta no se repita en la lista
            if pregunta in lista:
                pass
    #si la pregunta ya está en la lista se regresará al ciclo sin pasar a los otros condicionales
            elif pregunta == 1:
                print("P1.Encuentra la media aritmética de la siguiente lista de números [90, 98, 80, 70, 60, 90]")
                print("90\n 81\n 91\n 100")
    #se registra la respuesta
                resp1 = int(input("Introduzca la respuesta correcta: "))
    #se agrega el numero de pregunta a la lista
                lista.insert(0,pregunta)
            elif pregunta == 2:
                print("P2.¿Cúal es la moda en una serie de números? [2, 4, 1, 2, 4, 2, 8, 9, 1, 4, 5, 2]")
                print("4\n 1\n 2\n 9")
                resp2 = int(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 3:
                print("P3.Encuentre la mediana del conjunto [2, 5, 8, 11, 16, 21, 30]")
                print("11\n 8\n 2\n 30")
                resp3 = int(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 4:
                print("P4.Encuentra la media aritmética de la siguiente lista de números [9, 9, 8, 7, 6, 9]")
                print("8\n 9\n 8.5\n 6")
                resp4 = int(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            elif pregunta == 5:
                print("P5.Encuentre la mediana del conjunto [30, 60, 11, 45, 56, 20, 10, 32, 50, 62]")
                print("38\n 20\n 11\n 56")
                resp5 = int(input("Introduzca la respuesta correcta: "))
                lista.insert(0,pregunta)
            else:
                pass
    #se le llama a otra función para mostrar la califiación
        calificacionm(resp1, resp2, resp3, resp4, resp5)

    def calificacionm(resp1, resp2, resp3, resp4, resp5):
    #se usarán condicionales para evaluar las respuestas que se recibieron
        if resp1 == 81:
            x1 = 1
            print("P1: Respuesta correcta ☻")
        else:
            x1 = 0
            print("P1: UPPS... Respuesta incorrecta :c")
        if resp2 == 2:
            x2 = 1
            print("P2: Respuesta correcta ☻")
        else:
            x2 = 0
            print("P2: UPPS... Respuesta incorrecta :c")
        if resp3 == 11:
            x3 = 1
            print("P3: Respuesta correcta ☻")
        else:
            x3 = 0
            print("P3: UPPS... Respuesta incorrecta :c")
        if resp4 == 8:
            x4 = 1
            print("P4: Respuesta correcta ☻")
        else:
            x4 = 0
            print("P4: UPPS... Respuesta incorrecta :c")
        if resp5 == 38:
            x5 = 1
            print("P5: Respuesta correcta ☻")
        else:
            x5 = 0
            print("P5: UPPS... Respuesta incorrecta :c")
    #se hae un promedio de lo que se obtuvo para después mostrar la calificación en terminos de 0/100
        calificacion = ((x1 + x2 + x3 + x4 + x5)/5)*100 
        print("Su calificación fue de: ", calificacion)
    #se ejecuta la función en el código general
    preguntasm()    
    

elif tema == 4:
    print(nombre + " escogiste Despejar x de Ecuaciones, ¡mucha suerte!\n")
    #Sección: Despejar x de ecuaciones     
    print("El juego consiste en ir contenstando las preguntas que se te presenten, y se te iran sumando puntos si contestas de manera correcta")
    #Contador para ir sumando puntos si la respuesta se responde correcta
    puntos = 0
    #Se crea lista con preguntas para ir imprimiendo cada una a su vez
    preg = ["x + 5 = 13", "x - 9 = 17", "-3 + 4x = 9", "2 - 5x = -23", "-14x - 43 = -29", "-7x - 98 = 56",
            "8x - 12 = 4 + 4x", "3x + 24 - 5x = x", "1/3x + 2 = -5", "2/5x + 4 = x - 2"]
    #Se crea lista con respuestas para compararlas con el input del usuario
    resp = [8, 26, 3, 5, -1, -22, 4, 8, -21, 10]
    #Se crea ciclo para pasar cada pregunta de la lista y luego se compara con respuesta, si está correcta se van sumando 10 puntos
    for i in range(0, 10):
        print(preg[i])
        x = input("x = ")
        if esnumero(x) == True:
            x = int(x)
        else:
            print("Valor invalido, favor de ingresar sólo números enteros")
        if x == resp[i]:
            puntos = puntos + 10
        print("puntos: ", puntos)
    #Al final se da calificación, si aprueba se avisa al usuario que está listo para el examen, si no se recomienda seguir practicando
    if puntos >= 70:
        print("\n¡Felicidades, haz pasado el juego con un puntaje de ", puntos, "! Ya estás listo para tu exámen.")
    else:
        print("\nObtuviste un puntaje de ", puntos, ", te recomendamos seguir prácticando. ¡Tu puedes!")
        
        
elif tema == 5:
    print(nombre + " escogiste Razones/Ratios, ¡mucha suerte!\n")
    #Sección: Razones/Ratios
    #se imprimen instrucciones para el juego, el cual se deben contestar problemas matematicos para obtener pistas y resolver un acertijo
    #para resolver el acertijo hay que poner las letras de un código, que al final será "japon", estas letras se van agregando en cada paso
    contrasena = []
    print("Hola " + nombre)
    archivo = open('tesoro.txt','r')
    for i in archivo:
        print(i)
    archivo.close()
    """
    tesoro.txt imprime lo siguiente: Necesito tu ayuda. He encontrado una caja con un tesoro, pero no la puedo abrir ya que tiene una contraseña, que solo tú me puedes
    ayudar a encontrar. Para hacerlo, deberás responder a las siguientes preguntas, y si las sacas bien vas a obtener una pista que te
    va a ayudar a poder averiguar cada letra de la contraseña. ¡Tú puedes!
    """
    #pregunta 1, se pide la respuesta correcta, si esta bien se da la pista, si está mal se debe adivinar
    print("\nPregunta 1\n En un salón de clases hay 16 mujeres y 14 hombres. \n ¿Cuál es la razón de hombres contra mujeres?")
    print("a) 14/30 // b) 14/16 // c) 14/6 ")
    resp1 = input("Escribe la letra aquí: ")
    if resp1 == "b":
        print("¡Respuesta correcta! Pista: Decima letra del abecedario")
    else:
        print("Respueta equivocada, tendrás que adivinar primera letra sin pista :(")
    #se pide letra la cual se agrega a la lista llamada contrasena, donde el string se pasa a minusculas y se quitan espacios
    pista1 = input("Dame primera letra de la contraseña del tesoro: ")
    pista1 = (pista1.lower()).strip()
    contrasena.append(pista1)

    #pregunta 2, se pide la respuesta correcta, si esta bien se da la pista, si está mal se debe adivinar
    print("\nPregunta 2\n En una fiesta asistieron 22 jóvenes y 30 adultos. ¿Cuál es la razón de adultos contra el total?")
    print("a) 22/52 // b) 22/30 // c) 30/52 ")
    resp2 = input("Escribe la letra aquí: ")
    if resp2 == "c":
        print("¡Respuesta correcta! Pista: Primer letra del país donde viven los kanguros")
    else:
        print("Respueta equivocada, tendrás que adivinar primera letra sin pista :(")
    #se pide letra la cual se agrega a la lista llamada contrasena, donde el string se pasa a minusculas y se quitan espacios
    pista2 = input("Dame segunda letra de la contraseña del tesoro: ")
    pista2 = (pista2.lower()).strip()
    contrasena.append(pista2)

    #pregunta 3, se pide la respuesta correcta, si esta bien se da la pista, si está mal se debe adivinar
    print("\nPregunta 3\n Una tienda vende zapatos, donde la razón de pares de zapatos blancos a negros es de 1/4.")
    print("Si hay 15 pares de zapatos blancos, cuántos pares de zapatos negros hay en la tienda?")
    print("a) 45 // b) 60 // c) 15 ")
    resp3 = input("Escribe la letra aquí: ")
    if resp3 == "a":
        print("¡Respuesta correcta! Pista: Primera letra de la capital de Francia")
    else:
        print("Respueta equivocada, tendrás que adivinar primera letra sin pista :(")
    #se pide letra la cual se agrega a la lista llamada contrasena, donde el string se pasa a minusculas y se quitan espacios
    pista3 = input("Dame tercera letra de la contraseña del tesoro: ")
    pista3 = (pista3.lower()).strip()
    contrasena.append(pista3)

    #pregunta 4, se pide la respuesta correcta, si esta bien se da la pista, si está mal se debe adivinar
    print("\nPregunta 4\n La razón de estudiantes locales a estudiantes foráneos en un aula es de 5/8. Si hay 78 personas, cuántos estudiantes locales hay?")
    print("a) 30 // b) 24 // c) 50 ")
    resp4 = input("Escribe la letra aquí: ")
    if resp4 == "a":
        print("¡Respuesta correcta! Pista: Primera letra del nombre del único Premio Nobel de Literatura en México")
    else:
        print("Respueta equivocada, tendrás que adivinar primera letra sin pista :(")
    #se pide letra la cual se agrega a la lista llamada contrasena, donde el string se pasa a minusculas y se quitan espacios
    pista4 = input("Dame segunda letra de la contraseña del tesoro: ")
    pista4 = (pista4.lower()).strip()
    contrasena.append(pista4)

    #pregunta 5, se pide la respuesta correcta, si esta bien se da la pista, si está mal se debe adivinar
    print("\nPregunta 5\n La razón de un nieto y su abuelo es de 2 a 7. Las edades de ambos suman 63. Encuentra la edad del nieto.")
    print("a\) 49 // b\) 22 // c\) 14 ")
    resp5 = input("Escribe la letra aquí: ")
    if resp5 == "c":
        print("¡Respuesta correcta! Pista: Letra número 14 en el abecedario")
    else:
        print("Respueta equivocada, tendrás que adivinar primera letra sin pista :(")
    #se pide letra la cual se agrega a la lista llamada contrasena, donde el string se pasa a minusculas y se quitan espacios
    pista5 = input("Dame segunda letra de la contraseña del tesoro: ")
    pista5 = (pista5.lower()).strip()
    contrasena.append(pista5)
    #ya que se tienen todas las letras, se unen de la lista para hacer un sólo string
    password_final = "".join(contrasena)
    #se verifica que la contraseña del tesoro esté bien
    if password_final == "japon":
        print("\nFelicidades, lograste abrir el tesoro")
    else:
        print("\nLamentablemente, la contraseña estaba equivocada. ¡No te rindas!")
    print("Tu contraseña fue", password_final)
