import time
from lamp_options import *
import os

inputFile = os.path.join('.', 'lampinput')
lines = []
def main():
    try:
        with open(inputFile, 'r') as f:
            for line in f:
                line = line.strip().upper()
                lines.append(line)
                match line:
                    case 'TURN ON': lights_on()
                    case 'TURN OFF': lights_off()
                    case 'TOGGLE': lights_toggle()
                    case 'END':
                        print('Exiting program.')
                        exit()
            if 'END' not in lines:
                print(f'WARNING, file didn\'t end in \"END\".')
    except Exception as e:
        if FileNotFoundError:
            print(f'File {inputFile} not found.')
        else:
            print(e)

main()