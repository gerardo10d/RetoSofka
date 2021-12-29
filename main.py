#------------------------------------------------------------------------# de la correcta
import random
from preguntas import categorias
from Jugador import Jugador
from manejohistorial import leer, escribir

while True:

    opcion = input('Bienvenido.\nPresione 1 para jugar, 2 para ver el historial y 3 para salir\n')

    if opcion == '1':
        jugador1 = Jugador(input('Bienvenido jugador nuevo. Ingrese su nombre: '))

        for cat in categorias:
            pregunta = cat[random.randint(1,5)]
            print(f'Pregunta de categoría {cat[0]} (Premio: {cat[6]}):\n{pregunta[0]}',
                  '\nRespuestas:',
                  '\n1. ', pregunta[1],
                  '\n2. ', pregunta[2],
                  '\n3. ', pregunta[3],
                  '\n4. ', pregunta[4])
            respuesta = int(input('Escoja su respuesta (1, 2, 3, 4, 0 para retirarse del juego): '))
            if respuesta == pregunta[5]:
                print('¡Respuesta correcta!')
                jugador1.acumularPremio(cat[6])
                print(f'El premio acumulado hasta el momento es de: {jugador1.getPremio()}')
            elif respuesta == 0:
                print(f'El jugador {jugador1.getNombre()} se ha retirado del juego.'
                      f' El premio conseguido es de {jugador1.getPremio()}')
                break
            else:
                jugador1.setPremio(0)
                print(f'Respuesta incorrecta. Fin del juego.\nEl premio obtenido es de {jugador1.getPremio()}')
                break

        escribir(jugador1)

    elif opcion == '2':
        leer()
    else:
        break