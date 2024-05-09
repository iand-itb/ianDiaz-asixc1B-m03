"""
Ian Díaz
09/05/2024
ASIXc1 UF3 A1
Descripció: Examen Pp1
"""
import os
from logger import *

def clearFiles():
    try:
        files = ['paraules-2.txt', 'paraules-4.txt', 'paraules-6.txt', 'paraules-8.txt', 'paraules-10.txt']
        cleared = []
        for file in files:
            if os.path.exists(os.path.join('.', file)):
                cleared.append(file)
                os.remove(os.path.join('.', file))
        logger('warning', f'Output files ({str(cleared)}) cleared before continuing')
    except Exception as e:
        logger('error', f'Failed to clear output files: {e}')
def saveWord(words):
    try:
        logger('info', f'Sorting the words into each output file...')
        for word in words:
            charLength = len(list(word))
            if charLength % 2 == 0 and charLength <= 10:
                with open(f'paraules-{charLength}.txt', 'a') as f:
                    f.write(f'{word}\n')
        logger('info', f'Finished sorting the words. Time elapsed until now: {timeElapsed():.5f}')
    except Exception as e:
        logger('error', f'Failed to sort the words into each output file: {e}')

