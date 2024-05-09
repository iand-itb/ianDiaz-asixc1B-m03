"""
Ian Díaz
09/05/2024
ASIXc1 UF3 A1
Descripció: Examen Pp1
"""
import os
from logger import *

inputFile = os.path.join('.', 'paraules.txt')
words = []

def getData():
    try:
        with open(inputFile, 'r') as f:
            for line in f:
                line = line.strip().lower()
                words.append(line)
        logger('info', f'Data loaded successfully from file: {inputFile}, time to load: {timeElapsed():.5f} ')
        return words
    except Exception as e:
        logger('error', f'An exception was raised: {e}')
