def escribir(jugador):
    try:
        archivo = open('historial.txt', 'a', encoding='utf8')
        archivo.write('Nombre: ' + jugador.getNombre() + '; Premio: ' + str(jugador.getPremio()) + '\n')
    except Exception as e:
        print(e)
    finally:
        archivo.close()

def leer():
    try:
        archivo = open('historial.txt', 'r', encoding='utf8')
        print(archivo.read())
        archivo.close()
    except Exception as e:
        print(e)
