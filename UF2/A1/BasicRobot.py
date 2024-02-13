vel = 1
pos = [0.0, 0.0]

def main():
    command = input('Comando: ').upper()
    while True:
        match command:
            case 'DRETA':
                vector = ['X', pos[0] + vel]
                robot_move(vector)
            case 'ESQUERRA':
                vector = ['X', pos[0] - vel]
                robot_move(vector)
            case 'DALT':
                vector = ['Y', pos[1] + vel]
                robot_move(vector)
            case 'BAIX':
                vector = ['Y', pos[1] - vel]
                robot_move(vector)
            case 'ACCELERAR':
                robot_accelerate('+')
            case 'DISMINUIR':
                robot_accelerate('-')
            case 'POSICIO':
                print(f'La posició del robot és: ({pos[0]}, {pos[1]})')
            case 'VELOCITAT':
                print(f'La velocitat del robot és: {vel}')
            case 'HELP':
                print(f'Comandos:\n\tPOSICIO: Muestra la posición del robot\n\tVELOCITAT: Muestra la velocidad del robot.\n\tACCELERAR: Aumenta por 0.5 la velocidad del robot.\n\tDISMINUIR: Disminuye por 0.5 la velocidad del robot.\n\tDALT: Mueve el robot hacia arriba. (teniendo en cuenta la velocidad)\n\tBAIX: Mueve el robot hacia abajo. (teniendo en cuenta la velocidad)\n\tDRETA: Mueve el robot hacia la derecha. (teniendo en cuenta la velocidad)\n\tESQUERRA: Mueve el robot hacia la izquierda. (teniendo en cuenta la velocidad)\n\tEND: Acaba el programa.\n')
            case 'END':
                break
            case _:
                print("Vector incorrecto")
        command = input('Comando: ').upper()


def robot_move(vector):
    global pos
    match vector[0]:
        case 'X': pos[0] = vector[1]
        case 'Y': pos[1] = vector[1]
        case _: print("Vector incorrecto")


def robot_accelerate(mode):
    global vel
    if vel <= 10:
        if mode == '+':
            vel += 0.5
        else:
            vel -= 0.5

main()