"""
Ian Díaz
09/05/2024
ASIXc1 UF3 A1
Descripció: Examen Pp1
"""
import os
from logger import *

outFile = os.path.join('.', 'paraulesQuantitatVocals.txt')
VOWELS = 'aàáâeèéêiìíîoóòôuùúû'
vowelsPlusWord = []
def countVowels(words):
    try:
        logger('info', 'Starting to count the vowels for each word')
        for word in words:
            count = 0
            word = list(word)
            for char in word:
                if char in VOWELS:
                    count +=1
            word = ''.join(word)
            vowelsPlusWord.append(f'{count}\t{word}')
        logger('info', f'Finished counting the vowels, total time elapsed: {timeElapsed():.5f}')
        return vowelsPlusWord
    except Exception as e:
        logger('error', f'Failed to count the vowels for each word: {e}')
def writeVowelsPlusWord(countpluswords):
    try:
        logger('info', f'Starting to write the vowel count and words to the output file')
        with open(outFile, 'w') as f:
            for word in countpluswords:
                if word == countpluswords[-1]:
                    f.write(f'{word}')
                else:
                    f.write(f'{word}\n')
        logger('info' ,f'Finished writing the vowel count and words, total time elapsed: {timeElapsed():.5f}')
    except Exception as e:
        logger('error', f'Failed to save the words and their vowel count to the output file: {e}')