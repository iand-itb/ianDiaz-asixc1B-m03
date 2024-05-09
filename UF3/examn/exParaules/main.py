"""
Ian Díaz
09/05/2024
ASIXc1 UF3 A1
Descripció: Examen Pp1
"""
import os
import logging
import datainput
import task1, task2
from logger import *
def sigint(sig, frame):
    logger('info', f'Program ended early due to SIGINT (CTRL+C), done in {timeElapsed():.5f}')
    exit(2)

def main():
    try:
        logger('info', f'Starting program...')
        # TASK 1
        words = datainput.getData()
        task1.clearFiles()
        task1.saveWord(words)
        # TASK 2
        vowelspluswords = task2.countVowels(words)
        task2.writeVowelsPlusWord(vowelspluswords)
        logger('info', f'Program finished, total time elapsed: {timeElapsed():.5f}')
    except Exception as e:
        print(e)
main()