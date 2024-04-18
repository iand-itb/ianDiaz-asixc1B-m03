import logging
import os
import time
import signal


startTime = time.time()
logFile = os.path.join('.', 'dirRecursiu.log')
logFormat = '%(asctime)s %(levelname)s %(message)s'
logLevel = logging.DEBUG
logMode = 'at'

logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)

logging.info('Starting program.')

def def_handler(sig, frame):
    endTime = time.time()
    elapsed = endTime - startTime
    logging.info('Ending program due to SIGINT, time elapsed: %.3f\n', elapsed)
    exit(0)
signal.signal(signal.SIGINT, def_handler)

def recorrer_arbol_directorios(directorio):
    try:
        # Obtener la lista de archivos y directorios en el directorio actual
        contenido = os.listdir(directorio)

        # Recorrer cada elemento del directorio actual
        for elemento in contenido:
            # Crear la ruta completa del elemento
            ruta_elemento = os.path.join(directorio, elemento)

            # Si el elemento es un directorio, recorrer recursivamente
            if os.path.isdir(ruta_elemento):
                print("Directorio:", ruta_elemento)
                recorrer_arbol_directorios(ruta_elemento)

            else:
                print("Archivo:", ruta_elemento)
    except Exception as e:
        print(e)
        logging.error(f': {e}')


# Función principal

def main():
    # Solicitar al usuario el directorio inicial
    #directorio_inicial = input("Introduce la ruta del directorio inicial: ")
    directorio_inicial = '/'
    # Verificar si el directorio ingresado existe
    if not os.path.isdir(directorio_inicial):
        print(f"El directorio especificado no existe: {directorio_inicial}")
        logging.error(f'Directory not found: \'{directorio_inicial}\'')
    else:
        # Llamar a la función recursiva para recorrer el árbol de directorios
        print("\nRecorrido del árbol de directorios:")
        recorrer_arbol_directorios(directorio_inicial)


if __name__ == "__main__":
    main()
    endTime = time.time()
    elapsed = endTime - startTime
    logging.info('Ending program, time elapsed: %.3f\n', elapsed)