import random
import sys
# Lista de preguntas, respuestas y respuestas correctas
questions = list(zip( 
    [
        "¿Qué función se usa para obtener la longitud de una cadena en Python?",
        "¿Cuál de las siguientes opciones es un número entero en Python?",
        "¿Cómo se solicita entrada del usuario en Python?",
        "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
        "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
    ],
    [
        ("size()", "len()", "length()", "count()"),  
        ("3.14", "'42'", "10", "True"),
        ("input()", "scan()", "read()", "ask()"),
        ("// Esto es un comentario", "/* Esto es un comentario */",
         "-- Esto es un comentario", "# Esto es un comentario",),
        ("=", "==", "!=", "==="),
    ],
    [1, 2, 0, 3, 1]
))
# El usuario deberá contestar 3 preguntas
puntos_total = 0.0
# Se selecciona una pregunta aleatoria SIN repetir
questions_to_ask = random.sample(questions, 3)
# Se muestra la pregunta y las respuestas posibles
for question, options, answer_correct in questions_to_ask:
    print (question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
        #confirmo que la entrada sea un numero

        if not user_answer.isdigit():
            print("respuesta no valida")
            sys.exit(1)

        answer = int(user_answer) -1    
# Se verifica si la respuesta es correcta
        if answer < 0 or answer > 3:
            print("Respuesta no valida")
            sys.exit(1)

        if answer == answer_correct:
            print("¡Correcto!")
            puntos_total = puntos_total + 1.0
            break
        else:
            puntos_total = puntos_total - 0.5
    else:
# Si el usuario no responde correctamente después de 2 intentos,
# se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(options[answer_correct])
# Se imprime los puntos finales del jugador
print("el puntaje del jugador es de: ", puntos_total)
